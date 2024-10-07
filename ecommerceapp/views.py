from django.shortcuts import render,redirect
from ecommerceapp.models import Contact,product,OrderUpdate,Order
from django.contrib import messages
from django.http import HttpResponse
from math import ceil
from ecommerceapp import keys
from django.conf import settings
#MERCHANT_KEYS='kbzk1DSbJiV_O3p5' #Need to Create a Merchant account and then fill these KEY
import json 
from django.views.decorators.csrf import csrf_exempt
from paytm import checksum

from django.core.mail import send_mail
from ecommerce.settings import EMAIL_HOST_USER



def index(request):
    allprods=[]
    catprods = product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides =n // 4 + ceil(n/4) - (n //4)
        allprods.append([prod,range(1,nSlides),nSlides])

    param={'allprods':allprods}

    return render (request,'index.html',param)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        pnumber = request.POST.get("pnumber")
        print(pnumber)
        myquery = Contact(name=name, email=email, desc=desc, phonenumber=pnumber)
        myquery.save()
        messages.info(request, "We will get back to you soon...")
        return render(request, "contact.html")

    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")


def checkout(request):
    print (request)
    if not request.user.is_authenticated:
            messages.warning(request, "Login & Try Again")
            return redirect('/auth/Login')
    
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt', '')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = order(items_json=items_json, name=name, amount=amount, email=email, 
                address1=address1, address2=address2, city=city, state=state, 
                zip_code=zip_code, phone=phone)
        print(amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id,update_desc="Your Order has been Placed")
        update.save()
        thank=True

        #PAYMENT INTEGRATION

        id = Order.order_id
        oid=str(id)+"ApnaShop"
        param_dict = {
             
            'MID': keys.MID,
            'ORDER_ID':(oid),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handleresquest/',
        }

        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict,)# MERCHANT_KEY   )
        return render(request, "paytm.html", {'param_dict': param_dict})
    
    return render(request, "checkout.html")

@csrf_exempt
def handlerequest(request):
       
        # paytm will send you post request here
        form = request.POST
        response_dict = {}
        for i in form.keys():
            response_dict[i] = form[i]  
            if i == 'CHECKSUMHASH':
                checksum = form[i]

        verify = checksum.verify_checksum(response_dict, checksum)
        if verify:
            if response_dict['RESPCODE'] == '01':
                print('order successful')
                a= response_dict["ORDERID"]
                b=response_dict["TXNAMOUNT"]
                rid=a.replace("ApnaShop","")

                print(rid)
                filter2 = Order.objects.filter(order_id=rid)
                print(filter2)

                print(a, b)
                for post1 in filter2:
                    post1.amountpaid = b
                    post1.paymentstatus = "PAID"
                    post1.save()

                print("run agede function")

            else:
                print('order was not successful because' + response_dict['RESPMSG'])
            return render(request, 'paymentstatus.html', {'response': response_dict})


        
def profile(request):
    if not request.user.is_authenticated:
            messages.warning(request, "Login & Try Again")
            return redirect('/auth/Login')
    currentuser=request.user.username
    #print(currentuser)
    items=Order.objects.filter(email=currentuser)
    rid=""
    for i in items:
        print(i.oid)
        myid=i.oid
        rid=myid.replace("ApnaShop","")
        print (rid)
    status=OrderUpdate.objects.filter(order_id=int(rid))

    context={"items":items}
    for j in status:
         print(j.update_desc)
         print(j.deliverd)
         print(j.timestamp)
         context.update({"msg":j.update_desc})
         context.update({"dstatus":j.deliverd})
         context.update({"timestamp":j.update_desc})

    print (context)


   
    return render(request,"profile.html")