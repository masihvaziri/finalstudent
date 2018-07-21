from django.shortcuts import render
from studentSelection.forms import lessonsForm
from django.views import View
from studentSelection.models import teacher,lessons,termDetails
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url="/login/"),name='dispatch')
class registerCourse(View) :
    def get(self, request):
        form = lessonsForm()
        return render(request, 'registerCourse.html', {'form': form})

    def post(self, request):
        form = lessonsForm(request.POST)
        t = teacher.objects.get(teacherId=request.user.username)
        t2 = form.cleaned_data['term']


        temp = lessons.objects.create(name=request.POST['name'],vahed=request.POST['vahed'],capacity=request.POST['capacity'],remain=request.POST['remain'],details=request.POST['details'],term=t2,teacherID=t)
        if temp :
            error = 'ثبت نام باموفقیت به پایان رسید.'
            return render(request, 'registerCourse.html', {'error': error , 'form':form})
        else:
            error = 'خطا در ثبت نام'
            return render(request, 'registerCourse.html', {'form': form,'error':error})
