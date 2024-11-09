"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import List, Any

from django.contrib import admin
from django.urls import path, include
from app import views  # Replace 'app' with the actual name of your Django app, such as 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ensure views.home exists in your views.py file
    path('',include("app.urls",namespace='app')),
]
