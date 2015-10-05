from django.db import models


class Basic_detail(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sid = models.IntegerField()
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    DOB = models.DateField()
    father_name = models.CharField(max_length=200, default="")
    mother_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=100, default="")


class Course_detail(models.Model):
    cnum = models.CharField(max_length=9)
    cname = models.CharField(max_length=50)
    credits = models.IntegerField()
    year_of_registration = models.BigIntegerField()
