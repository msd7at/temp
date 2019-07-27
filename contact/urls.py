from contact import views
from django.conf.urls import url

urlpatterns=[
url("feedback",views.feedback),
url("add",views.add),
]
