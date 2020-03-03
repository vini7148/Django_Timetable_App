"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = "app1"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'reg_page'),
    path('login/', views.login_re, name = 'log_page'),
    path('logout/', views.logout_request, name  = "logout_page"),
    path('class/', views.cla, name = 'class'),
    path('classall/', views.classes, name = 'classes'),
    path('teacher/', views.tea, name = 'teacher'),
    path('user/', views.ur, name = 'user'),
]
