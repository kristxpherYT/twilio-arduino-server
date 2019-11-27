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

    account_sid = '<TWILIO SID>'
  
    auth_token = '<TWILIO AUTH TOKEN>'
  
    client = Client(account_sid, auth_token)
    
    requestData = request.POST['Body']
    temperature = Data.objects.last().temperature
    humidity = Data.objects.last().humidity

    if (requestData == 'Temp'):
        client.messages.create(
            body='Temperature: ' + temperature + ' °C',
            from_='whatsapp:<TWILIO SANDBOX NUMBER>',
            to='whatsapp:<YOUR WHATSAPP NUMBER>')
    elif (requestData == 'Hum'):
        client.messages.create(
            body='Humidity: ' + humidity + ' %',
            from_='whatsapp:<TWILIO SANDBOX NUMBER>',
            to='whatsapp:<YOUR WHATSAPP NUMBER>')
    elif (requestData == 'All'):
        client.messages.create(
            body='Temperature: ' + temperature + ' °C\nHumidity: ' + humidity + ' %',
            from_='whatsapp:<TWILIO SANDBOX NUMBER>',
            to='whatsapp:<YOUR WHATSAPP NUMBER>')

    data = {
        'temperature': temperature,
        'humidity': humidity
    }

    return JsonResponse(data, safe=False)

@csrf_exempt
def recordData(request):
    data = Data(
        temperature=request.POST['temperature'],
        humidity=request.POST['humidity']
        )
    data.save()

    return JsonResponse({'message': 'success'}, safe=False)