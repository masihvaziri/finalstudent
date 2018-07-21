from django.shortcuts import render
from django.views import View
from studentSelection.models import teacher
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url="/login/"),name='dispatch')
class hometeacher (View):
    def get(self,request):
        firstName = request.user.first_name
        lastName = request.user.last_name
        teacher1 = teacher.objects.filter(teacherId=request.user.username).first()
        return render(request,"hometeacher.html",{'teacher':teacher1})