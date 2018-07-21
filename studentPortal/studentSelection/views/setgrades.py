from django.shortcuts import render
from django.views import View
from studentSelection.models import lessons,termDetails,selections,grades
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url="/login/"),name='dispatch')
class setgrades (View):
    def get(self,request):
        return render(request,"setgrades.html")


    def post(self,request):

        coursId = None
        lessonList = None
        try:
            lessonId = request.POST['lessonId']
            studentId = request.POST['studentId']
        except:
            try:
                coursId = request.POST['inputvalue']
            except:
                try:
                    yearSearch = request.POST['YearSearch']# 2018
                    termSearch = request.POST['optionSearch'] # 2
                    temp = int(yearSearch)+1
                    name = "%s%s%s"%(yearSearch,temp,termSearch)
                    request.session['term_name'] = name
                    request.session['yearSearch'] = yearSearch
                    request.session['termSearch'] = termSearch

                    termj = termDetails.objects.filter(name=name).first()
                    lessonList = lessons.objects.filter(teacherID__teacherId=request.user.username, term=termj).all()

                    return render(request, "setgrades.html", {'lessonList': lessonList,'yearSearch':yearSearch,'termSearch':termSearch})
                except:
                    return render(request, "setgrades.html",{ 'lessonList': lessonList})


        if(coursId != None):
            studentList = selections.objects.filter(lessonID__lessonID= coursId).all()


        else:
            studentList = selections.objects.filter(lessonID__lessonID=lessonId).all()
            n = studentList.count()
            for std in studentList :
                if request.POST[std.studentCode.studentCode]:
                    temp1 = std.studentCode  # student
                    temp2 = request.POST[std.studentCode.studentCode] # grade for student
                    answer =  request.POST['protest'+std.studentCode.studentCode]
                    selections.objects.filter(studentCode= temp1 , lessonID = std.lessonID).update(gradeValu = float(temp2))
                    grades.objects.filter(studentCode=temp1,lessonID = std.lessonID).update(gradeValue=float(temp2),protestAnswer=answer)

            studentList = selections.objects.filter(lessonID__lessonID=lessonId).all()

        termj = termDetails.objects.filter(name=request.session['term_name']).first()
        lessonList = lessons.objects.filter(teacherID__teacherId=request.user.username, term=termj).all()
        return render(request, "setgrades.html", {'lessonList': lessonList ,'students':studentList })