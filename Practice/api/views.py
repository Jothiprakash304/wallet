from django.shortcuts import render
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.response import Response
from .serializer import First,Addserializer,Withdraw,add_card
from datetime import timedelta
from .models import Cloud_22,Cloud_2,card,transaction_timing,transaction_add_timing
from django.contrib.auth.hashers import check_password
import bcrypt
from django.contrib.auth.backends import ModelBackend
from .forms import myform
from django.contrib.sessions.models import Session
from django.dispatch import Signal, receiver
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail,BadHeaderError
import logging
from django.contrib.auth.decorators import login_required
from .tasks import send_email_task,otp_send

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from datetime import timedelta
from .serializer import practice
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

logger=logging.getLogger(__name__)
# Create account api
@api_view(['POST'])
def create_user(request):
    serializer=First(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        refresh_time=RefreshToken.for_user(user)
        refresh_time.access_token.set_exp(lifetime=timedelta(seconds=30))
        token=str(refresh_time.access_token)
        request.session['serializer']=token
        send_email_task.delay(user.Email)
        return Response({"token":token},status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)





# User Login api
@api_view(['POST'])
def login_user(request):
    Email = request.data.get("Email")
    Password = request.data.get("Password")
    try:
        user = Cloud_2.objects.get(Email=Email)
        stored_hash = user.Password
        if check_password(Password, stored_hash):
            request.session['Email'] = Email
            user,created=User.objects.get_or_create(username=user)
            token,_=Token.objects.get_or_create(user=user)
            request.session['token'] = token.key
            return Response({'success':'done'})
    except Cloud_2.DoesNotExist:
        pass

    return Response('Email or password incorrect')

# user update api

        
# user delete api
@api_view(['DELETE'])
def delete_user(request,pk):
    token=request.session.get("token")
    if token:
        try:
            a=Cloud_2.objects.filter(Email=pk)
            a.delete()
            return Response({'message':"User account deleted successfully"})
        except Exception as e:
            return Response({'Message': 'Transaction failed.','error':str(e)})
    else:
        return Response("Authentication Failed")
    

# add money module api
@api_view(['PUT'])
def add_money(request):
    Email=request.session.get('Email')
    token=request.session.get('token')
    if token:
        try:
            user_cloud2 = Cloud_2.objects.get(Email=Email)
        except Cloud_2.DoesNotExist:
            return Response('User not found')
        try:
            user=Cloud_22.objects.get(Email=Email)
        except Cloud_22.DoesNotExist:
            return Response('User not found')
        serializer=Addserializer(instance=user,data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
           return Response(serializer.errors)
    else:
        return Response('User not logged in')
    
# withdraw money module api
@api_view(['PUT'])
def withdraw(request):
    Email=request.session.get('Email')
    token=request.session.get('token')
    if token:
        try:
            user=Cloud_2.objects.get(Email=Email)
        except Cloud_2.DoesNotExist:
            return Response('user not found')
        
        try:
            user_1=Cloud_22.objects.get(Email=user)
        except Cloud_22.DoesNotExist:
            return Response('user not found')
        serializer=Withdraw(instance=user_1,data=request.data)
        if serializer.is_valid():
            a=serializer.save()
            return Response({"status":'success'})
        else:
            return Response(str(serializer.errors))
    else:
        return Response('User not Logged in')
    

@api_view(['PUT'])
def add_card_details(request):
    Email=request.session.get('Email')
    token=request.session.get('token')
    if token:
        if Email:
            try:
                user=Cloud_2.objects.get(Email=Email)
            except Cloud_2.DoesNotExist:
                return Response('user not found')
            try:
                a=card.objects.get(Email=user)
            except :
                return Response('User not found')
            if a.card_present==False:
                serializer=add_card(instance=a,data=request.data)
                if serializer.is_valid():
                        a=serializer.save()
                        return Response(status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors)
            else:
                return Response("Card details are already added")
        else:
            return Response('User not Logged in')
    else:
        return Response("Authentication Failed")
# fetch balance api
@api_view(['GET'])
def balance(request):
    Email=request.session.get('Email')
    a=Cloud_22.objects.get(Email=Email)
    Balance=a.Amount
    return JsonResponse({'balance':Balance})

# transaction details for Add money
@api_view(['GET'])
def add_details(request):
    Email=request.session.get('Email')
    token=request.session.get("token")
    if token:
        details=transaction_timing.objects.filter(Email=Email).values('id','Email','Date','Time','Amount')
        return Response(details)
    else:
        return Response("Authentication Failed")
    
# transaction details for withdraw money
@api_view(['GET'])
def withdraw_details(request):
    Email=request.session.get('Email')
    token=request.session.get("token")
    if token:
        details=transaction_add_timing.objects.filter(Email=Email).values('id','Email','Date','Time','Amount')
        return Response(details)
    else:
        return Response("Authentication Failed")
    

@api_view(['POST'])
def request_otp(request):
    Email=request.data.get('Email')
    if not Email:
        return Response({'error':"Email is required for verification"})
    otp_send.delay(Email)
    return Response({'Message':"OTP sent successfully "},status=status.HTTP_200_OK)

@api_view(['GET'])
def user_detail(request):
    Email=request.session.get("Email")
    token=request.session.get("token")
    if token:
        if Email:
            fetch_details=Cloud_2.objects.filter(Email=Email).values("Name","Mobile","Date")
            return Response(fetch_details)
        else:
            return Response({"Message":"something Wrong"})
    else:
        return Response({"Message":"User not logged in"})



# user logout api   
@api_view(['POST'])
def logout_view(request):
    logout(request)
    request.session.flush()
    return Response({'message':'success'})



def view(request):
    return render(request,'crud/Register.html')
def Login(request):
    return render(request,'crud/Login.html')

def Home(request):
    return render(request,'crud/Home.html')
def Forgot(request):
    return render(request,'crud/forgot.html')


def Add(request):
    return render(request,'Banking/add_money.html')
def form(request):
    form=myform()
    return render(request,'crud/sum.html',{'form':form})

def dash(request):
    return render(request,'Banking/Dashboard.html')


def withdraw_1(request):
     return render(request,'Banking/withdraw.html')


def send(request):
    return render(request,'banking/send_money.html')

def trans(request):
    return render(request,'Banking/transaction_for_add.html')