from django.http import HttpResponse
from django.shortcuts import render , HttpResponse
from django.contrib.staticfiles import storage
from abhi.models import contact
# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST['name']
        email= request.POST['email']
        number= request.POST['number']
        message = request.POST['message']
        #print(name,email,number,message)
        ins= contact(name=name,email=email,number=number,message=message)
        ins.save()
        print("uploaded to database")
    return render(request,"index.html")
