from accounts import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name = 'home'),
    path('about/', views.AboutPageView, name = 'about'),
    path('test/', views.TestPageView, name = 'test'),
    path('design/',views.DesignerPageView, name = 'design'),
    path('sales/', views.SalesPage , name = 'sales'),
    path('managment/',views.ManagmentPageView , name = 'managment'),
]
