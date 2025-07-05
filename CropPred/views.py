from urllib import request
from django.shortcuts import render
import pickle
from django.conf import settings
import os


#creating views for the urls
#views are functions that take a request and return a response

model = os.path.join(settings.BASE_DIR, 'rfc.pkl')
with open(model, 'rb') as file:
    model = pickle.load(file)

def home(request):
    pred=None
    if request.method == "POST":
        temp = request.POST['temp']
        humidity = request.POST['humidity']
        ph = request.POST['ph']
        water = request.POST['water']

        print("Temperature:", temp)
        print("Humidity:", humidity)        
        print("pH:", ph)
        print("Water:", water)

        env=[[temp,humidity,ph,water]]
        pred = model.predict(env)
    return render(request, "home.html",{'prediction':pred})


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")