from studentSelection.models import students,selections,lessons,grades,termDetails
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render

@login_required(login_url="/login/")
def choiceCourse(request):
    coursid = lessons.objects.get(lessonID=request.GET['lesson_id'])
    studentid = students.objects.filter(studentCode=request.user.username).first()

    selected_cours = selections.objects.filter(lessonID=coursid,studentCode=studentid,lessonID__term =coursid.term )  # check shavad ke dars mored nazar ghabla entekhab nashode bashad
    all_selected_cours = selections.objects.filter(studentCode=studentid,lessonID__term =coursid.term )  # vahed haue entekhabi daneshjo dar term jari

    if (selected_cours.count() == 0):
        termLesson = lessons.objects.filter(term__lessons__details = selected_cours.first())

        if coursid.remain > 0:
            count = sum(c.lessonID.vahed for c in all_selected_cours) + coursid.vahed
            if count <= 20:
                gradeF = grades.objects.create(lessonID=coursid , studentCode=studentid,gradeValue=0)
                selections.objects.create(lessonID=coursid, studentCode=studentid, dateReg=datetime.now(),gradeFK=gradeF)

                coursid.remain = coursid.remain - 1
                coursid.save()
                massage = "درس مورد نظر(%s) با موفقیت انتخاب شد." % coursid.name
            else:
                massage = "شما مجاز به انتخاب بیش از 20 واحد نمی باشید"
        else:
            massage = "ظرفیت درس مورد نظر(%s)تکمیل شده است. امکان انتخاب وجود ندارد." % coursid.name

    else:
        massage = "شما قبلا درس مورد نظر(%s) را انتخاب کرده اید." % coursid.name


    term = lessons.objects.get(lessonID= coursid.lessonID).term.name # term jari
    all_lesson = lessons.objects.filter(term__name=term).order_by('lessonID') # drose term jari
    selected = selections.objects.filter(studentCode=studentid ,lessonID__term__name= term) #drose entekhabi term jari
    count = sum (c.lessonID.vahed for c in selected)

    return render(request, 'entekhabVahed.html', {'student_id'
                : studentid.studentCode, 'all_lesson': all_lesson, 'selected': selected, 'error':massage , 'count':count})