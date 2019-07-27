from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    res=render(request,"hksmain/menu.html")
    return res
def LIST(request):
    res=render(request,"hksmain/LIST.html")
    return res
