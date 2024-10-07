from django.db import models 

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class product(models.Model):
    product_id = models.CharField(max_length=50, unique=True)  
    product_name = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=50, default="")
    price  = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/media/images") 

    def __str__(self):
        return self.product_id
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    oid = models.CharField(max_length=50, blank=True)
    amountpaid = models.CharField(max_length=500, blank=True, null=True)
    paymentstatus = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    deliverd=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.update_desc[0:7] + " ..."


