"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import contrib
from django import urls
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User managment this includes a lot of pages for account managemnt 
    # can be seen in official auth doc
    path('accounts/', include('django.contrib.auth.urls')),
    # local apps
    path('accounts/', include('accounts.urls')),
    path('', include('main_app.urls')),
    
]
