from django.db import models
from django.db.models import Count,Sum,Avg,ExpressionWrapper,F,DecimalField,Q,Case,When
from abc import ABC, abstractmethod
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import transaction

# Create your models here.

class Cloud_2(models.Model):
    Email=models.EmailField(primary_key=True,max_length=30,unique=True)
    Name=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    Password=models.CharField(max_length=100)
    Date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Table_2'
class Cloud_22(models.Model):
    Email=models.ForeignKey(Cloud_2,on_delete=models.CASCADE)
    Amount=models.IntegerField()
    class Meta:
        db_table='amount_table_1'
# withdraw_table
class transaction_add_timing(models.Model):
    Email=models.ForeignKey(Cloud_2,on_delete=models.CASCADE)
    Date=models.DateField(auto_now_add=True)
    Time=models.TimeField(auto_now_add=True)
    Amount=models.IntegerField()
    class Meta:
        db_table='Transaction_details'
# add_money table
class transaction_timing(models.Model):
    Email=models.ForeignKey(Cloud_2,on_delete=models.CASCADE)
    Date=models.DateField(auto_now_add=True)
    Time=models.TimeField(auto_now_add=True)
    Amount=models.IntegerField()
    class Meta:
        db_table='Add_money_history'

# card details
class card(models.Model):
    Email=models.ForeignKey(Cloud_2,on_delete=models.CASCADE)
    Card_number=models.BigIntegerField()
    Expiry=models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
              regex=r'^\d{2}/\d{2}$',
              message='Expiry date must be in the format of "MM/YY"'
            )
        ]
    )
    CVV=models.IntegerField()
    name=models.CharField(max_length=30)
    card_present=models.BooleanField(default=False)
    class Meta:
        db_table="card_details"




















        





   




