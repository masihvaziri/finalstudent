from django.shortcuts import render ,redirect
from studentSelection.forms import studentRegisterForm
from django.contrib.auth import login,authenticate
from django.views import View
from django.contrib.auth.models import User
from studentSelection.models import students,teacher

class mylogin(View):

    def get(self,request):
        form = studentRegisterForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):

        form = studentRegisterForm(request.POST)
        password = request.POST['password']
        username = request.POST['studentCode']
        stu = students.objects.filter(studentCode=username)
        thc = teacher.objects.filter(teacherId=username)


        user = authenticate(request,username=username,password=password)
        if (user is not None):
            if (user.is_active):
                login(request,user)
                if stu.count() != 0 :
                    return redirect('/home/')
                else:
                    return redirect('/hometeacher/')
            else:
                return render(request, 'login.html', {'error': "کاربر غیر فعال است. ", 'form': form})
        else:
            return render(request, 'login.html', {'error': "نام کاربری و یا رمز ورود اشتباه است.", 'form': form})