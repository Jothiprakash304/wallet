from rest_framework import serializers
from django.db.models import F,Sum
from api.models import Cloud_22,Cloud_2,card
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import bcrypt
from django.contrib.auth.hashers import make_password
from django.db import transaction
from .signals import withdraw_signal,add_signal
import re

class practice(serializers.ModelSerializer):
    class Meta:
        model=Cloud_2
        fields=("Email","Name","Mobile")
    def validate(self,data):
        if not data["Email"]:
            raise serializers.ValidationError("Email ")
    def create(self,validated_data):
        validated_data.pop("Confirm_password",None)
        Password=validated_data.pop("Password",None)
        hashed=make_password(Password)
        validated_data["data"]=hashed
        a=Cloud_2.objects.create(**validated_data)
        b=Cloud_2.objects.get(Email=a.Email)
        instance=Cloud_22.objects.create(Amount=0,Email=b)
# create user serializer
class First(serializers.ModelSerializer):
    Confirm_password=serializers.CharField(write_only=True)
    class Meta:
        model=Cloud_2
        fields=('Email','Name','Mobile','Password','Confirm_password','Date')
    def validate(self,data):
        if not data["Email"]:
            raise serializers.ValidationError("Email is mandatory")
        if not data["Name"]:
            raise serializers.ValidationError("Name is mandatory")
        if not data["Mobile"]:
            raise serializers.ValidationError("Mobile is mandatory")
        if data["Password"]!=data["Confirm_password"]:
            raise serializers.ValidationError('Password Mismatch_1')
        return data
    def create(self,validated_data):
        validated_data.pop("Confirm_password",None)
        Password=validated_data.pop("Password",None)
        hashed=make_password(Password)
        validated_data["Password"]=hashed
        a=Cloud_2.objects.create(**validated_data)
        b=Cloud_2.objects.get(Email=a.Email)
        cloud_instance=Cloud_22.objects.create(Amount=0,Email=b) and card.objects.create(Email=b,Card_number=0,Expiry='00/00',CVV=0,name='name')
        return cloud_instance
    
# update user serializer



# Add money module serializer
class Addserializer(serializers.ModelSerializer):
    class Meta:
        model=Cloud_22
        fields=('Amount',)
    def validate(self,data):
        if data['Amount']<=0:
            raise serializers.ValidationError('Minimum amount is required')
        return data
    def update(self,instance,validated_data):
        amount=validated_data["Amount"]
        a=instance.Email
        instance.Amount +=amount
        instance.save()
        add_signal.send(sender=a,sender_1=amount)
        return instance

# withdraw money module serilaizer
class Withdraw(serializers.ModelSerializer):
    class Meta:
        model=Cloud_22
        fields=('Amount',)
    def validate(self,data):
        current_amount=self.instance.Amount
        if data['Amount']>current_amount:
            raise ValidationError('Your account balance is low')
        elif data['Amount'] is None:
            raise ValidationError('Please enter the amount')
        return data
    def update(self,instance,validated_data):
        amount=validated_data['Amount']
        
        a=instance.Email
        interest=(amount/100)*5
        deduction_amount=interest+amount
        instance.Amount -=deduction_amount
        instance.save()
        withdraw_signal.send(sender=a,sender_1=amount)
        return instance
   
    
# Add card details serializer
class add_card(serializers.ModelSerializer):
    class Meta:
        model=card
        fields=("Card_number","Expiry","CVV","name","card_present")
    def validate(self,data):
        card_number=data['Card_number']
        expiry=data['Expiry']
        cvv=data['CVV']
        name=data['name']
        regex=r'^\d{2}/\d{2}$'
        if len(str(card_number))!=16:
            raise ValidationError('Enter the valid card number')
        if not re.fullmatch(regex,expiry):
            raise ValidationError('Your card is expired')
        if len(str(cvv))!=3:
            raise ValidationError("Please enter the valid cvv number")
        if not name.isalpha():
            raise ValidationError('Please enter the valid name as per in your card')
        return data
    def create(self,validated_data):
        return card.objects.update(**validated_data)
        
















    # def save(self):
    #      a=Cloud(
    #           Email=self.validated_data["Email"],
    #           Name=self.validated_data["Name"],
    #           Mobile=self.validated_data['Mobile'],
    #           Password=self.validated_data["Password"]
    #      )
    #      Password=self.validated_data["Password"]
    #      Confirm_password=self.validated_data["Confirm_password"]
    #      if Password!=Confirm_password:
    #          return Res("Password Mismatch")
    #      a.save()
    #      return a




        # if data['Password']!=data["Confirm_password"]:
        #     raise ValidationError("Password Mismatch")
        # return


    
    
 





        # Email=self.validated_data['Email']
        # Name=self.validated_data['Name']
        # Mobile=self.validated_data['Mobile']
        # Password=self.validated_data['Password']
        # Confirm_password=self.validated_data['Confirm_password']
        # if Email is None:
        #     raise ValidationError({"Error":"Please enter the Email"})
        # if Name is None:
        #     raise ValidationError({"Error":"Name is mandatory"})
        # if Mobile is None and len(Mobile)<=9:
        #     raise ValidationError({'Error':'Mobile number should be in required credentials'})
        # if Password!=Confirm_password:
        #     raise ValidationError({"Error":"Password Mismatch"})
        # salt=bcrypt.gensalt(10)
        # password=Password.encode('utf-8')
        # hash=bcrypt.hashpw(password,salt)
        # Password=hash



          # def validate(self,data):
    #     Email=data.get("Email")
    #     Name=data.get("Name")
    #     Mobile=data.get("Mobile")
    #     Password=data.get("Password")
    #     Confirm_password=data.get("Confirm_password")

    #     if not Email:
    #         raise ValidationError("Email is not present")
    #     if not Name:
    #         raise ValidationError("Name is not present")
    #     if not Mobile:
    #         raise ValidationError("Mobile is not present")
    #     if Password!=Confirm_password:
    #         raise ValidationError("Password mismatch")
    #     return data

        
