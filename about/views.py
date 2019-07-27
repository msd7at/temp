from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aboutus(request):
    res=render(request,"about/about.html")
    return res
# Create your views here.
