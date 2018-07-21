from django.contrib.auth.models import User
from django.db import models

class allUser(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    # class Meta:
    #      db_table = 'allUser'
