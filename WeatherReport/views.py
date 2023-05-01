from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def hello(request):

    if request.method == "POST":
        location =request.POST.get('city')
        url = "https://api.weatherapi.com/v1/current.json?key=adedddcf1b334f9dbfc102056233103&q="+location+"&aqi=no"
        
        
        data = requests.get(url)
        if data.status_code == 200:

            data=data.json()
            
            return render(request, "home.html", {'location':data['location'], 'current':data['current'],})

        else:
            message = "Invalid City Name"
            return render(request, "home.html", {'message':message})
            
    else:
        stat=0
        return render(request, "home.html", {'stat':stat})
