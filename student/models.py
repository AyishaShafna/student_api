from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length = 100)   #these are column/attributes in table
    age = models.BigIntegerField()
    gender = models.CharField(max_length = 20)
    mobile = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    class Meta:
        db_table = 'student'