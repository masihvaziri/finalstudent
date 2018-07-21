from django.contrib.auth import logout
from django.shortcuts import redirect


def mylogout(request):
    try:
        logout(request)
    finally:
        return redirect('/login/')