from django.forms import ModelForm
from studentSelection.models import lessons


class lessonsForm (ModelForm) :

    class Meta:
        model = lessons
        fields = ['lessonID','name','teacherID','vahed','capacity','remain','details','term']


