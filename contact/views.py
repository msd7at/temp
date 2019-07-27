
# Create your views here.
from contact import models
from django.shortcuts import render
from django.http import HttpResponse
from contact.forms import feedbackform
def feedback(request):
    form=feedbackform()
    res=render(request,"contact/contact.html",{'form':form})
    return res

def add(request):
    if request.method=="POST":
        form=feedbackform(request.POST)
        info= models.info()
        info.iname=form.data["iname"]
        info.iage=form.data["iage"]
        info.iemail=form.data["iemail"]
        info.imsg=form.data["imsg"]
        info.save()
    s="feedback send successfully"
    return HttpResponse(s)
