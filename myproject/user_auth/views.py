# Replace 'your_twilio_account_sid' and 'your_twilio_auth_token' with your actual Twilio credentials, and '+12345678901' with your actual Twilio number. Make sure that the phone numbers are in E.164 format. 
from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
import random

User = get_user_model()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone_number = request.POST['phone_number']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already taken')

        # Create user
        user = User(username=username, phone_number=phone_number)
        user.set_password(password)
        user.save()

        # Generate and send verification code
        verification_code = random.randint(1000, 9999)
        request.session['verification_code'] = verification_code
        request.session['username'] = username

        # Send verification code via SMS using Twilio
        account_sid = 'your_twilio_account_sid'
        auth_token = 'your_twilio_auth_token'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f'Your verification code is {verification_code}',
            from_='+12345678901',  # Your Twilio number
            to=phone_number
        )

        return HttpResponse('Verification code sent')
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def verify(request):
    if request.method == 'POST':
        verification_code = request.POST['verification_code']

        # Check verification code
        if verification_code == request.session['verification_code']:
            # Mark user as active
            username = request.session['username']
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()

            return HttpResponse('Verification successful')
        else:
            return HttpResponse('Incorrect verification code')
    else:
        return HttpResponse('Invalid request')
