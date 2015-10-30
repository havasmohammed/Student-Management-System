from django.contrib import admin

from .models import BasicDetail, CourseDetail, LoginPage, AcademicDetail, MiscellaneousDetail
from .forms import BasicDetailForm, CourseDetailForm, LoginPageForm, MiscellaneousDetailForm, AcademicDetailForm


class LoginPageAdmin(admin.ModelAdmin):
    list_display = ('sid', 'password')
    form = LoginPageForm

    class Meta:
        model = LoginPage
admin.site.register(LoginPage, LoginPageAdmin)


class BasicDetailAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'middle_name',
                    'last_name',
                    'sid',
                    'gender',
                    'address',
                    'DOB',
                    'father_name',
                    'mother_name',
                    'email',
                    'blood_group',
                    'father_profession',
                    'family_income',
                    'religion',
                    'caste',
                    'reservation_category',
                    'emergency_contact_number')
    form = BasicDetailForm

    class Meta:
        model = BasicDetail
admin.site.register(BasicDetail, BasicDetailAdmin)


class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ('cname',
                    'stream',
                    'code',
                    'year_of_registration',
                    'duration',
                    'level')
    form = CourseDetailForm

    class Meta:
        model = CourseDetail
admin.site.register(CourseDetail, CourseDetailAdmin)


class AcademicDetailAdmin(admin.ModelAdmin):
    list_display = ('Attendence_percentage',
                    'cname',
                    'First_year_percentage_of_marks',
                    'Second_year_percentage_of_marks',
                    'Third_year_percentage_of_marks',
                    'Fourth_year_percentage_of_marks',
                    'Total_percentage_of_marks',
                    'Class_awarded')
    form = AcademicDetailForm

    class Meta:
        model = AcademicDetail
admin.site.register(AcademicDetail, AcademicDetailAdmin)


class MiscellaneousDetailAdmin(admin.ModelAdmin):
    list_display = ('nss',
                    'ncc',
                    'sports',
                    'hobbies',
                    'personal_website',
                    'orkut_profile_url',
                    'facebook_profile_url',
                    'linkedin_profile_url')
    form = MiscellaneousDetailForm

    class Meta:
        model = MiscellaneousDetail
admin.site.register(MiscellaneousDetail, MiscellaneousDetailAdmin)
