from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from studentSelection.models import students ,grades ,lessons,termDetails

@method_decorator(login_required(login_url="/login/"),name='dispatch')
class amozesh(View) :
    def get(self,request):

        student_id_object = students.objects.filter(studentCode=request.user.username).first()
        listofterm = termDetails.objects.filter(startTime__gte=student_id_object.dateReg).all().order_by('name')
        return render(request, "amozesh.html",{'name': request.user.first_name, 'family': request.user.last_name , 'listofterm':listofterm})

    def post(self,request):

        student = students.objects.filter(studentCode=request.user.username).first()
        listofterm = termDetails.objects.filter(startTime__gte=student.dateReg).all().order_by('name')

        try:
            term = request.POST['inputvalue']
        except:
            prot = request.POST['protest']
            protlessonId = request.POST['protestLessonId']
            term = lessons.objects.filter(lessonID=protlessonId).first().details
            grades.objects.filter(studentCode = student , lessonID__lessonID=protlessonId).update(protest=prot)


        grade = grades.objects.filter(studentCode=student )
        totalavg = 0
        N=0
        for item in grade :
            if item.gradeValue != 0 :
                totalavg = totalavg + item.gradeValue * item.lessonID.vahed
                N = N + item.lessonID.vahed
        try:
            totalavg = totalavg/N
        except:
            totalavg = 0


        grade = grades.objects.filter(studentCode=student,lessonID__term__name=term)
        avg = 0
        N = 0
        for item in grade :
            if item.gradeValue != 0:
                avg = avg + item.gradeValue * item.lessonID.vahed
                N = N + item.lessonID.vahed
        try:
            avg = avg/N
        except:
            avg = 0

        return render(request,"amozesh.html",{'name': request.user.first_name, 'family': request.user.last_name ,'grade':grade , 'avg':avg , 'totalavg':totalavg,'listofterm':listofterm})