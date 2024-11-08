from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    phones=Products.objects.filter(phone=True)
    dress=Products.objects.filter(dress=True)
    return render(request, 'index.html',{'phones':phones,'dress':dress})

def secpage(request,id):
    product=Products.objects.get(id=id)
    return render(request, 'secpage.html',{'product':product})