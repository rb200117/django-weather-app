from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from decouple import config
import json
import urllib.request
import requests
from datetime import date
# import environ

# env = environ.Env()
# # reading .env file
# environ.Env.read_env()

# Create your views here.
def weatherCompute(request):
    submitButton = request.POST.get("submit")
    form = NameForm(request.POST or None)
    if form.is_valid():
        cityName = form.cleaned_data.get("cityName")
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityName+'&appid='+config('APP_KEY')
    data = requests.get(url).json()
    temp = float(data['main']['temp'])
    temp = temp - 273.15
    feelTemp = float(data['main']['feels_like'])
    feelTemp = feelTemp - 273.15
    print(feelTemp)

    
    
    context = {'city': cityName, 'submitbutton': submitButton, "country_code": str(data['sys']['country']),
               "coordinate": str(data['coord']['lon']) + ' '
               + str(data['coord']['lat']),
               "temp": str(round(temp, 2)) + '°C',
               "pressure": str(data['main']['pressure']),
               "humidity": str(data['main']['humidity'])+' %', 
               "feels_like": str(round(feelTemp, 2))+'°C',}
    return render(request, 'weatherApp/info.html', context)

def show(request):
    if request.method=='POST':
        form = NameForm(request.POST)
    else:
        form=NameForm()
    return render(request, 'weatherApp/form.html',{'form':form})

