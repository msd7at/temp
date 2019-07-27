from hksmain import views
from django.conf.urls import url

urlpatterns=[
    url("menu",views.menu),
    url("LIST",views.LIST),
]
