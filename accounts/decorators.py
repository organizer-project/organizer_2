from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            Group = None
            if request.user.groups.exists():
                Group = request.user.groups.all()[0].name
            if Group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                print(Group)
                return HttpResponse('not authorised to see this page')
        return wrapper_func
    return decorator