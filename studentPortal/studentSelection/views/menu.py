from django.shortcuts import render
from studentSelection.models import students
from django.contrib.auth.decorators import login_required

# @login_required()
def menu(request) :
    student = students.objects.get(studentCode='8875')
    return render(request,"menu.html",{'user':student})