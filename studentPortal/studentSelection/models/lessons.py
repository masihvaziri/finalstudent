from django.db import models
from .teacher import teacher
from .termDetails import termDetails

class lessons(models.Model) :
    # lessonID = models.CharField(max_length=10,default="1234")
    lessonID = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=30)
    teacherID = models.ForeignKey(teacher , on_delete=models.CASCADE )
    details = models.CharField(null=True, max_length=50,default="")
    vahed = models.IntegerField()
    capacity =models.IntegerField()
    remain = models.IntegerField()
    term = models.ForeignKey(termDetails , on_delete=models.CASCADE )

    # examTime = models.DateTimeField()


    def __str__(self):
        return self.name
    #
    # class Meta:
    #     db_table ='lessons'
    #
