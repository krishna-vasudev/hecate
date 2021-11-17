from .tokens import account_activation_token
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import Patient,Medical





UserModel = get_user_model()

# Create your views here.

def loginUser(request,usertype):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            if(usertype == "patient"):
                return render(request, "accounts/patientsignup.html")
            elif(usertype == "medical"):
                return render(request, "accounts/hospsignin.html")

    if(usertype=="patient"):
        return render(request, "accounts/patientsignup.html")
    elif(usertype=="medical"):
        return render(request, "accounts/hospsignin.html")
    

def logoutuser(request):
    logout(request)
    return redirect('/')

def signupuser(request,usertype):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already in use')
            return redirect('/')
        elif username == "":
            messages.warning(request, 'Invalid Username')
            return redirect('/')
        elif password == "":
            messages.warning(request, 'Invalid Password')
            return redirect('/')
        else:
            try:
                validate_email(email)
            except ValidationError as e:
               messages.warning(request, 'Invalid email address')
               return redirect('/')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                user.is_active = False
                user.save()
                if usertype=='patient':
                    full_name=request.POST.get('fullname')
                    new_patient=Patient(patient=user,full_name=full_name)
                    new_patient.save()
                elif usertype=='medical':
                    name= request.POST.get("medicalname")
                    location=request.POST.get('location')
                    new_medical=Medical(medical=user,name=name,location=location)
                    new_medical.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('accounts/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                messages.success(
                    request, 'Please confirm your email address to complete the registration')
                return redirect('/')

    if(usertype == "patient"):
        return render(request, "accounts/patientsignup.html")
    elif(usertype == "medical"):
        return render(request, "accounts/hospsignin.html")

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('/')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('/')
