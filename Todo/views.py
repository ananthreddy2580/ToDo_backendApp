# from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
from django.contrib.auth.hashers import make_password,check_password
from .models import*
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view


# from rest_framework_simplejwt.tokens import RefreshToken
# @csrf_exempt
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrftoken': token})



def home(request):
    return HttpResponse("Welcome to the Visitor API! Use /visitors/ to submit data.")


@csrf_protect
def sign_in(request):
    if request.method == "POST":
        try:
            sign_in_data = json.loads(request.body)
            email = sign_in_data.get("email")
            password = sign_in_data.get("password")

            if not email or not password:
                return JsonResponse({"message": "Both email and password are required", "status": "failed"})

            user = UserRegistration.objects.filter(user_email=email).first()
            if user:
                if check_password(password, user.password):
                    return JsonResponse({"message": "Login successful", "status": "success"})
                else:
                    return JsonResponse({"message": "Password does not match", "status": "failed"})

            return JsonResponse({"message": "User not found", "status": "failed"})

        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({"message": "Data transfer failed", "status": "failed"})
     
@csrf_protect
def sign_up(request):
    if request.method == "POST":
        try:
            sign_up_data = json.loads(request.body)
            fullname = sign_up_data.get("fullname")
            email = sign_up_data.get("email")
            password = sign_up_data.get("password")
            hashedPassword = make_password(password)

            user = UserRegistration.objects.create(
                user_fullname=fullname,
                user_email=email,
                password=hashedPassword,
            )
            return JsonResponse({"message": "User Created Successfully","status":"failed"})
        except Exception as e:
            # print("Error:", str(e))
            return JsonResponse({"message": "User Created Failed","status":"failed"})

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


@csrf_protect
@api_view(['POST'])
def send_reset_link(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        user = UserRegistration.objects.filter(user_email=email).first()
        if user:
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = f"http://localhost:5173/reset-password/{uidb64}/{token}" 
            send_mail(
                subject="Password Reset for Your App",
                message=f"""Hi {user.user_fullname},

                You requested to reset your password.

                Please click the link below to reset:

                {reset_url}

                Thank you,
                The ToDo Team
                """,
                        from_email="pythonmail17@gmail.com",
                        recipient_list=[email],
                        fail_silently=False,
                )
        return JsonResponse ({"message":"Email sent","status":"success"})
    except Exception as e:
        print(e)
        return JsonResponse({"message": "Failed to send reset link", "status": "failed"})
    
@csrf_protect
@api_view(['POST'])
def update_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserRegistration.objects.get(pk=uid)
        if user == None:
           return JsonResponse({"message": "User Doesn't Exist", "status": "failed"})
        if user is not None and default_token_generator.check_token(user, token):
            data = json.loads(request.body)
            new_password = data.get("password")
            user.password = make_password(new_password) 
            user.save()
            return JsonResponse({"message": "Password Updated", "status":"success"})
        else:
            return JsonResponse({"message": "Invalid or Expired Token", "status":"failed"})
    except Exception as e:
        print("Error while resetting password:", str(e))
        return JsonResponse({"message": "Failed to update password", "status": "failed"})