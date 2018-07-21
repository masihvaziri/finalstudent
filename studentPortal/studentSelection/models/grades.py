from django.db import models
from studentSelection.models import students ,lessons


class grades(models.Model):
    studentCode = models.ForeignKey(students, on_delete=models.CASCADE)
    lessonID = models.ForeignKey(lessons, on_delete=models.CASCADE)

    protest = models.TextField(null=True)
    protestAnswer = models.TextField(null=True)
    openProtest = models.BooleanField(default=True)
    gradeValue = models.FloatField(null=True)
    status = models.BooleanField(default=False)
    #
    # class Meta:
    #     db_table ='grades'