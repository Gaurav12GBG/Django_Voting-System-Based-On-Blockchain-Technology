from django.core.mail import send_mail
from django.conf import settings

def send_forget_password_mail(email, token):
    subject = "Your forget password link"
    message = f"Hi, Click on the lik to reset your password : http://127.0.0.1:8000/change_password/{token}/"
    email_from = "gauravgangurde456@gmail.com"
    print("COrrect one")
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
