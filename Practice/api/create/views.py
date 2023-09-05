from django.shortcuts import render,HttpResponse
from .models import Image,Password
import jwt
from django.http import JsonResponse
# Create your views here.
def view(request):
    username='jothiprakash'
    payload={'user':username}
    secret_key='123'
    token=jwt.encode(payload,secret_key)
    return JsonResponse({'token':token})