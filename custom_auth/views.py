from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import generate_token
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        # Check if passwords match
        if password != confirm_password:
            messages.warning(request, "Passwords do not match")
            return render(request, 'signup.html')

        # Check if email is already taken
        try:
            if User.objects.get(username=email):
                messages.warning(request, "Email is already taken")
                return render(request, "signup.html")
        except User.DoesNotExist:
            pass

        # Create a new user
        user = User.objects.create_user(email, email, password)
        user.is_active = False  # Set user as inactive until email confirmation
        user.save()

        # Send activation email
        email_subject = "Activate Your Account"
        email_body = render_to_string('activate.html', {
            'user': user,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
        })

        email_message = EmailMessage(email_subject, email_body, settings.EMAIL_HOST_USER, [email])
        email_message.send()

        messages.success(request, "Activate your account by clicking the link sent to your email")
        return redirect('/custom_auth/login/')

    return render(request, "signup.html")

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.info(request, "Account activated successfully")
            return redirect('/custom_auth/login')

        return render(request, 'custom_auth/activatefail.html')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']

        # Use the authenticate function to verify the credentials
        myuser = authenticate(username=username, password=userpassword)

        # Check if authentication was successful
        if myuser is not None:
            login(request, myuser)  # Log the user in
            messages.success(request, "Login Successful")
            return redirect('/')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/custom_auth/login')  # Reload the login page if credentials are wrong

    # If the request method is GET, render the login page
    return render(request, 'login.html')



def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Sucess")
    return redirect('/custom_auth/login')
