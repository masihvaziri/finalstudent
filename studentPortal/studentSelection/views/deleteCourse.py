from studentSelection.models import students,selections,lessons,grades
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render

@login_required(login_url='/login/')
def deleteCourse(request):
    massage=""
    coursid = lessons.objects.get(lessonID = request.GET['item_id'])
    studentid = students.objects.get(studentCode = request.user.username)

    selected_cours = selections.objects.filter(lessonID=coursid , studentCode=studentid )
    select_Course_Grade = grades.objects.filter(lessonID=coursid , studentCode=studentid )

    if (selected_cours.count != 0 ):
        selected_cours.all().delete()
        select_Course_Grade.all().delete()
        coursid.remain = coursid.remain + 1
        coursid.save()
        massage= "درس مورد نظر (%s) با موفقیت حذف شد." % coursid.name

    term = lessons.objects.get(lessonID=coursid.lessonID).term.name  # term jari
    all_lesson = lessons.objects.filter(term__name=term).order_by('lessonID')  # drose term jari
    selected = selections.objects.filter(studentCode=studentid, lessonID__term__name=term)  # drose entekhabi term jari
    count = sum(c.lessonID.vahed for c in selected)

    return render(request, 'entekhabVahed.html', { 'student_id'
    : studentid.studentCode, 'all_lesson': all_lesson, 'selected': selected, 'error':massage, 'count':count})