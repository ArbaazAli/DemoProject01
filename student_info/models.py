from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    First_Name = models.CharField(max_length=15, null=True)
    Last_Name = models.CharField(max_length=15)
    Contact = models.IntegerField()
    username = models.EmailField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15, null=True)
    Re_Password = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.username
