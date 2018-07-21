from django.shortcuts import render ,redirect
from studentSelection.forms import studentRegisterForm
from django.contrib.auth import login,authenticate,logout
from django.views import View
from django.contrib.auth.models import User
from studentSelection.models import teacher

class register(View):
    def get(self,request):
        form = studentRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = studentRegisterForm(request.POST , request.FILES)

        password = request.POST['password']
        username = request.POST['studentCode']
        email = request.POST['email']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']

        if (not User.objects.filter(username=username).exists()):
            try:
                if form.is_valid():
                    if request.POST['who'] == 'student':
                        b = form.save()
                        user = User.objects.create_user(username=username, password=password, email=email,
                                                        first_name=first_name, last_name=last_name)
                        login(request, user)
                        return redirect('/home/')
                    else:
                        teacher.objects.create(firstName=form.cleaned_data['firstName'],lastName=form.cleaned_data['lastName'],address=form.cleaned_data['address'],
                                               teacherId=form.cleaned_data['studentCode'],password=form.cleaned_data['password'],status=1,img=request.FILES['img'],
                                               email=form.cleaned_data['email'],mobile=form.cleaned_data['mobile'])

                        user = User.objects.create_user(username=username, password=password, email=email,
                                                        first_name=first_name, last_name=last_name)
                        del form
                        login(request, user)
                        return redirect('/hometeacher/')

                else:
                    error = "ورودی نامعتبر."
            except:
                return redirect('/logout/')
        else:
            error = "نام کاربری تکراری می باشد."

        return render(request, 'register.html', {'form': form, 'error': error})