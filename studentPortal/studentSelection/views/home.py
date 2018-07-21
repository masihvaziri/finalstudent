from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from studentSelection.models import students


@method_decorator(login_required(login_url="/login/"),name='dispatch')
class home(View) :

    def get(self,request):
        student = students.objects.filter(studentCode=request.user.username).first()
        return render(request, 'home.html', {'student':student})

    def post(self,request):
        return render(request, 'home.html')
