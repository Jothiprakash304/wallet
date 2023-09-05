from celery import shared_task
from django.core.mail import send_mail
import logging
import random
from django.core.cache import cache
logger=logging.getLogger(__name__)
@shared_task
def send_email_task(email):
    subject='Welcome to cloudpay wallet'
    message="Please read the content below carefully"
    from_email='kill87843@gmail.com'
    recipient=[email]
    try:
        send_mail(subject,message,from_email,recipient)
        logger.info(f"Email sent successfully to {email}")
        return True
    except Exception as e:
        logger.error(f"Failed to sent Email to {email}")
        return False

@shared_task
def otp_send(email):
    otp=generate_otp_code()
    cache_key=f'otp_{email}'
    cache.set(cache_key,otp,timeout=300)

    subject='OTP Verification'
    message=f"OTP for process the verification is {otp}"
    from_email='kill87843@gmail.com'
    recipient=[email]
    
    try:
        send_mail(subject,message,from_email,recipient)
        logger.info(f"OTP sent successfully to {email}")
        return True
    except Exception as e:
        logger.error(f"Failed to sent Email to {email}")
        return False
    
def generate_otp_code():
    otp=random.randrange(2000,4000)
    return otp


