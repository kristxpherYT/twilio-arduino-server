# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

# Create your views here.
@csrf_exempt
def tempHumData(request):
    # Your Account Sid and Auth Token from twilio.com/console
  
    account_sid = 'AC26f748d29bce5289dfbe6ea9d2e9faee'
  
    auth_token = '3a8fc6e6a07774fde54ab518b1c20743'
  
    client = Client(account_sid, auth_token)
    
    temperature = request.POST

    data = {
        'temperature': request.POST,
        'humidity': 'humidity'
    }

    client.messages.create(
        body='Temperature: ' + temperature,
        from_='whatsapp:+14155238886',
        to='whatsapp:+593979103931')

    return JsonResponse(data, safe=False)