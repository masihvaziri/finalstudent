from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from studentSelection.forms import studentRegisterForm
from studentSelection.models import students
from django.contrib.auth import login
from django.contrib.auth.models import User


@method_decorator(login_required(login_url="/login/"),name='dispatch')
class profile(View) :
    def get(self,request):
        student = students.objects.filter(studentCode=request.user.username).first()
        form = studentRegisterForm()
        return render(request,'profile.html',{'student':student ,'form':form})


    def post(self, request):
        form = studentRegisterForm(request.POST, request.FILES)
        confirmPassword = form.data['confirmPassword']
        user = User.objects.get(username=request.user.username)

        if confirmPassword == form.data['password']:
            student = students.objects.filter(studentCode=request.user.username).first()

            student.firstName = form.data['firstName']
            student.lastName = form.data['lastName']
            student.mobile = form.data['mobile']
            student.address = form.data['address']
            student.email = form.data['email']
            student.password = form.data['password']
            if form.files:
                student.img = form.files['img']
            student.save()

            user.first_name = form.data['firstName']
            user.last_name = form.data['lastName']
            user.set_password(confirmPassword)
            user.email = form.data['email']
            user.save()
            login(request, user)
            error = "ویرایش با موفقیت انجام گرفت"
        else:
            error = " تاییدیه رمز ورود با رمز ورود یکسان نمی باشد"

        return render(request, 'profile.html',
                      {'student': student,'error': error})