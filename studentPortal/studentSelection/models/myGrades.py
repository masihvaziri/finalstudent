from django.db import models

class myGrades(models.Model):

    gradeValue = models.FloatField(null=True)
    status = models.BooleanField(default=False)
    #
    # class Meta:
    #     db_table ='mygrades'