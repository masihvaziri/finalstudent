from django.db import models
from studentSelection.models import lessons,students,grades

class selections(models.Model) :

    lessonID = models.ForeignKey(lessons, on_delete=models.CASCADE)
    studentCode = models.ForeignKey(students, on_delete=models.CASCADE)
    gradeFK  = models.ForeignKey(grades, on_delete=models.CASCADE ,default=None)


    dateReg = models.DateTimeField(max_length=30)
    gradeValu = models.FloatField(null=True)

    # class Meta:
    #     db_table = "selections"
