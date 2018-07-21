from django.db import models
from datetime import datetime

class termDetails(models.Model):
    name = models.CharField(null=False,max_length=5) #96971
    detail = models.CharField(null=True,max_length=20)# نیم سال اول 96-97
    startTime = models.DateField(null=False,default=datetime.now)

    def __str__(self):
        return self.detail