from django.contrib import admin
from .models import *

class lessonsAdmin (admin.ModelAdmin):
    list_display = ['lessonID', 'name','teacherID', 'vahed', 'capacity','remain','details','term']

class studentsAdmin (admin.ModelAdmin):
    list_display = [ 'studentCode' ,'password','firstName', 'lastName', 'address','email','mobile', 'dateReg','img','status',]

class selectionsAdmin (admin.ModelAdmin):
    list_display = [ 'studentCode' ,'lessonID','dateReg',]

class gradesAdmin (admin.ModelAdmin):
    list_display = [ 'studentCode' ,'lessonID','gradeValue', 'status',]

class teacherAdmin (admin.ModelAdmin):
    list_display = [ 'teacherId' ,'firstName','lastName', 'status',]

class termDetailsAdmin (admin.ModelAdmin):
    list_display = [ 'name' ,'startTime']


admin.site.register(lessons,lessonsAdmin)
admin.site.register(students,studentsAdmin)
admin.site.register(selections,selectionsAdmin)
admin.site.register(grades,gradesAdmin)
admin.site.register(teacher,teacherAdmin)
admin.site.register(termDetails,termDetailsAdmin)
