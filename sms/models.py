from django.db import models
from builtins import str


class Login_page(models.Model):
    sid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=100)

    def is_authenticated(self):
        """
        The is_authenticated method has a misleading name. In general this method should
        just return True unless the object represents a user that should not be allowed
        to authenticate for some reason.
        """
        return True

    def is_active(self):
        """
        The is_active method should return True for users unless they are inactive,
        for example because they have been banned.
        """
        return True

    def is_anonymous(self):
        """
        The is_anonymous method should return True only for fake users that are not
        supposed to log in to the system.
        """
        return False

    def get_id(self):
        """
        Finally, the get_id method should return a unique identifier for the user, in unicode format.
        We use the unique id generated by the database layer for this.
        """
        return str(self.sid)


class Basic_detail(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sid = models.IntegerField(primary_key=True)
    id_card_number = models.CharField(max_length=50, default="", unique=True)
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
