from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from accounts.decorators import allowed_users
# Create your views here.

def HomePageView(request):
    return render(request, 'home.html')


def AboutPageView(request):
    return render(request, 'about.html')
    
def TestPageView(request):
    return render(request, 'test.html')



@login_required(login_url='account_login')
@allowed_users(allowed_roles=['Admin','Design'])
def DesignerPageView(request):
    return render(request, 'designer.html')

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['Admin','Managment'])
def ManagmentPageView(request):
    return render(request, 'managment.html')

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['Admin','Sales'])
def SalesPage(request):
    return render(request, 'sales.html')