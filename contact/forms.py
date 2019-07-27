from django import forms

class feedbackform(forms.Form):
    iname=forms.CharField(label="Name",max_length=35)
    iage=forms.IntegerField(label="Age")
    iemail=forms.CharField(label="E-Mail",max_length=35)
    imsg=forms.CharField(label="Message",max_length=1000)
