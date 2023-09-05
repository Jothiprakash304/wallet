"""Practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api import views as A

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a',A.create_user),
    path('v',A.view),
    path('l',A.login_user),
    path('login',A.Login,name='login'),
    path('home',A.Home,name='home'),
    path('forgot',A.Forgot,name='forgot'),
    path('sum',A.form,name='sum'),
    path('delete/<str:pk>',A.delete_user,name='delete'),
    path('add_money',A.add_money),
    path('add',A.Add,name='add'),
    path('logout',A.logout_view),
    path('withdraw',A.withdraw),
    path('add_card',A.add_card_details,name='add_card'),
    path('dash',A.dash),
    path('balance',A.balance),
    path('with',A.withdraw_1),
    path('send',A.send),
    path('details',A.add_details),
    path('trans',A.trans),
    path('w_details',A.withdraw_details),
    path('otp',A.request_otp),
    path("user_detail",A.user_detail)
]
