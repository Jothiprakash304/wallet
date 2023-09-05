from django.dispatch import Signal,receiver
from django.db.models.signals import post_save
from .models import transaction_add_timing,transaction_timing


withdraw_signal=Signal()

add_signal=Signal()

@receiver(withdraw_signal)
def handle(sender,sender_1,**kwargs):
    Email=sender
    Amount=sender_1
    transaction_add_timing.objects.create(Amount=Amount,Email=Email)

@receiver(add_signal)
def add(sender,sender_1,**kwargs):
    Email=sender
    Amount=sender_1
    transaction_timing.objects.create(Amount=Amount,Email=Email)