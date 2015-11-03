from django.db import models
from builtins import str
from django.contrib.auth.models import User
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.db.models import Avg

COURSE_LEVELS = (
    ('UG', 'Under Graduate'),
    ('PG', 'Post Graduate'),
    ('12th', '12th'),
    ('10th', '10th'),
    )

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )

BLOOD_GROUP_CHOICES = (
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    )

RESERVATION_CATEGORY_CHOICES = (
    ('OC', 'OC'),
    ('OBC', 'OBC'),
    ('MBC', 'MBC'),
    ('BC', 'BC'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    )

CLASS_AWARDED_LEVELS = (
    ('FIRST CLASS WITH DISTINCTION', 'FIRST CLASS WITH DISTINCTION'),
    ('FIRST CLASS', 'FIRST CLASS'),
    ('SECOND CLASS', 'SECOND CLASS'),
    ('PASS CLASS', 'PASS CLASS'),
    ('FAIL', 'FAIL'),
    )

BRANCH_CHOICES = (
    ('IT', 'IT'),
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('CE', 'CE'),
    ('PE', 'PE'),
    ('ME', 'ME'),
    ('AE', 'AE'),
    ('EE', 'EE'),
    ('BT', 'BT'),
    ('CHE', 'CHE')
    )

SEMESTER_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    )


class StudentProfile(models.Model):
    # Register Number, First Name and Last Name are defined in User model
    user = models.OneToOneField(User, unique=True,)

    @property
    def institution_name(self):
        return self.user.institution_name

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def full_name(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    @property
    def register_number(self):
        return self.user.username

    @property
    def last_login(self):
        return self.user.last_login


class LoginPage(models.Model):
    sid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=100)


class BasicDetail(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200)
    sid = models.IntegerField(primary_key=True)
    # id_card_number = models.CharField(max_length=50, default="", unique=True)
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES,
                              default='M')
    address = models.CharField(max_length=200)
    DOB = models.DateField()
    father_name = models.CharField(max_length=200, default="")
    mother_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=100, default="")
    blood_group = models.CharField(max_length=4, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
    father_profession = models.CharField(max_length=100, null=True, blank=True)
    family_income = models.IntegerField(null=True, blank=True)
    religion = models.CharField(max_length=30,
                                null=True, blank=True)
    caste = models.CharField(max_length=30,
                             null=True, blank=True)
    reservation_category = models.CharField(max_length=10,
                                            choices=RESERVATION_CATEGORY_CHOICES,
                                            null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=20, null=True, blank=True)

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s, %s %s' % (self.lastname, self.firstname, self.middlename)
    full_name = property(_get_full_name)


class CourseDetail(models.Model):
    cname = models.CharField(max_length=50, unique=True)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES, default="")
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES, default="")
    code = models.CharField(max_length=10, unique=True, help_text='Code of the stream', default="")
    year_of_registration = models.BigIntegerField()
    duration = models.IntegerField(help_text='Duration of the course in years', default=2)
    level = models.CharField(max_length=4,
                             choices=COURSE_LEVELS,
                             default='10th')

    objects = models.Manager()


class AcademicDetail(models.Model):
    attendence_percentage = models.DecimalField(max_digits=5,
                                                decimal_places=2,
                                                default=0)
    cname = models.CharField(max_length=50, default=''),
    first_year_percentage_of_marks = models.DecimalField(max_digits=5,
                                                         decimal_places=2,
                                                         default=0)
    second_year_percentage_of_marks = models.DecimalField(max_digits=5,
                                                          decimal_places=2,
                                                          default=0)
    third_year_percentage_of_marks = models.DecimalField(max_digits=5,
                                                         decimal_places=2,
                                                         default=0)
    fourth_year_percentage_of_marks = models.DecimalField(max_digits=5,
                                                          decimal_places=2,
                                                          default=0)
    total_percentage_of_marks = models.DecimalField(max_digits=5,
                                                    decimal_places=2,
                                                    default=0)
    # Total_percentage_of_marks = .rating_set.aggregate(Avg('stars')).values()[0]
    class_awarded = models.CharField(max_length=50,
                                     choices=CLASS_AWARDED_LEVELS,
                                     null=True, blank=True)


class MiscellaneousDetail(models.Model):
    nss = models.BooleanField(blank=True)
    ncc = models.BooleanField(blank=True)
    sports = models.CharField(max_length=100, null=True, blank=True)
    hobbies = models.CharField(max_length=100, null=True, blank=True)
    personal_website = models.URLField(null=True, blank=True)
    orkut_profile_url = models.URLField(null=True, blank=True)
    facebook_profile_url = models.URLField(null=True, blank=True)
    linkedin_profile_url = models.URLField(null=True, blank=True)
