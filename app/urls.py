from . import views
from django.urls import path,include

app_name="app"

urlpatterns=[
    path('', views.home , name='home'),
]