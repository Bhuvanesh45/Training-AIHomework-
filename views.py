from django.shortcuts import render
import requests,json

def home(request):
    url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Chennai'

    return render(request, 'home.html', {url})