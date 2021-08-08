from django.db import models

from django.db import models
class Course(models.Model):
    No = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Faculty = models.CharField(max_length=30)
    Date = models.DateField(auto_now_add=True)
    Time = models.CharField(max_length=20)
    Fee = models.IntegerField()
    Duration = models.CharField(max_length=30)

class Student(models.Model):
    No = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30, unique=True)
    Contact = models.IntegerField(unique=True)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=20)
class Enrolldetails(models.Model):
    Student_contact = models.IntegerField()
    Course_name = models.CharField(max_length=20,default=True)




