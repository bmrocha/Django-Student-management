from django.db import models

# Create your models here.


class Student(models.Model):
    student_number = models.PositiveIntegerField()
