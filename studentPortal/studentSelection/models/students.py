from django.db import models
from datetime import datetime
from studentSelection.extraTest.extra import ContentTypeRestrictedFileField
from .allUser import allUser

class students(models.Model) :
    # user = models.ForeignKey(allUser,on_delete=models.CASCADE)

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    studentCode = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    status = models.IntegerField(null=True) # 1-> activ  0-> deactive
    dateReg = models.DateTimeField( null=True ,default=datetime.now)
    img = ContentTypeRestrictedFileField(upload_to = 'images',content_types=['image/jpg', 'image/png', 'image/jpeg', ], max_upload_size_kb=150)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=11,null=True)
    # #
    # class Meta:
    #     db_table = "students"
    def __str__(self):
        return self.studentCode

