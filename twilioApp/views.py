# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from twilioApp.models import Data

# Create your views here.
@csrf_exempt
def tempHumData(request):
    # Your Account Sid and Auth Token from twilio.com/console
  
    account_sid = 'AC26f748d29bce5289dfbe6ea9d2e9faee'
  
    auth_token = '3a8fc6e6a07774fde54ab518b1c20743'
  
    client = Client(account_sid, auth_token)
    
    requestData = request.POST['Body']
    temperature = Data.objects.all()[0]['temperature']
    humidity = Data.objects.all()[0]['humidity']

    client.messages.create(
        body='Temperature: ' + requestData,
        from_='whatsapp:+14155238886',
        to='whatsapp:+593979103931'
    )
    if (requestData == 'Temp'):
        client.messages.create(
            body='Temperature: ' + temperature,
            from_='whatsapp:+14155238886',
            to='whatsapp:+593979103931')
    elif (requestData == 'Hum'):
        client.messages.create(
            body='Humidity: ' + humidity,
            from_='whatsapp:+14155238886',
            to='whatsapp:+593979103931')
    elif (requestData == 'All'):
        client.messages.create(
            body='Temperature: ' + temperature + '\nHumidity: ' + humidity,
            from_='whatsapp:+14155238886',
            to='whatsapp:+593979103931')

    data = {
        'temperature': temperature,
        'humidity': humidity
    }

    return JsonResponse(data, safe=False)

@csrf_exempt
def recordData(request):
    if (Data.objects.all()):
        Data.objects.all().delete()

    data = Data(
        temperature=request.POST['temperature'],
        humidity=request.POST['humidity']
        )
    data.save()

    return JsonResponse({'message': 'success'}, safe=False)