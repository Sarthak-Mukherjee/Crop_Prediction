"""
URL configuration for CropPred project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import home, about, contact
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(url, view_func, url_name)
    path("home",home, name="homepage"),
    path("about",about,name="aboutpage"),
    path("contact",contact,name="contactpage"),
]
