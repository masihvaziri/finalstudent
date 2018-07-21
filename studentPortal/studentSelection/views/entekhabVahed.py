from django.shortcuts import render_to_response, render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from studentSelection.models import students,lessons,selections,termDetails



@method_decorator(login_required(login_url="/login/"),name='dispatch')
class entekhabVahed (View):
    def get(self,request):
        try:
            student_id = request.user.username
            student_id_object = students.objects.filter(studentCode=student_id)[0]  # instance of students model

            listTerm = termDetails.objects.filter(startTime__gte= student_id_object.dateReg ).all().order_by('name')

            return render(request,'entekhabVahed.html', {'listTerm':listTerm})
        except:
            return redirect('/logout/')



    def post(self,request):
        student_id = request.user.username
        student_id_object = students.objects.filter(studentCode=student_id)[0]  # instance of students model
        term = request.POST['inputvalue']

        termLesson = lessons.objects.filter(term__name=term)

        student_choice_cours = selections.objects.filter(studentCode=student_id_object , lessonID__in=termLesson).order_by('lessonID')

        listTerm = termDetails.objects.filter(startTime__gte=student_id_object.dateReg).all().order_by('name')

        count = sum(c.lessonID.vahed for c in student_choice_cours)  # دروس انتخاب شده

        return render(request, 'entekhabVahed.html', {'all_lesson': termLesson, 'selected': student_choice_cours, 'count': count,
                                                      'listTerm': listTerm})

