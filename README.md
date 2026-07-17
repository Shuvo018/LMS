# Learning Management System


### send mali

first create a app from google account -> search (app password) -> then create account

```bash
# settings.py

#  Define the SMTP backend wrapper
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587              


EMAIL_USE_TLS = True 
EMAIL_USE_SSL = False

# Authentication credentials
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# Default sender email displayed to recipients
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")



# views.py
from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    send_mail(
        subject="Testing Django SMTP Setup",
        message="This is a test message sent automatically from my web application.",
        from_email=None,  # Passing None forces Django to default to DEFAULT_FROM_EMAIL
        recipient_list=["recipient@example.com"],
        fail_silently=False,  # Set to False to catch exceptions if authentication fails
    )
    return HttpResponse("Email successfully sent!")

```