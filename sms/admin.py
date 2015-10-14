from django.contrib import admin

from .models import Basic_detail, Course_detail, Login_page, Academic_detail, Miscellaneous_detail
from .forms import Basic_detailForm, Course_detailForm, Login_pageForm, Miscellaneous_detailForm


class Login_pageAdmin(admin.ModelAdmin):
    list_display = ('sid', 'password')
    form = Login_pageForm

    class Meta:
        model = Login_page
admin.site.register(Login_page, Login_pageAdmin)


class Basic_detailAdmin(admin.ModelAdmin):
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
    form = Basic_detailForm

    class Meta:
        model = Basic_detail
admin.site.register(Basic_detail, Basic_detailAdmin)


class Course_detailAdmin(admin.ModelAdmin):
    list_display = ('cname',
                    'stream',
                    'code',
                    'year_of_registration',
                    'duration',
                    'level')
    form = Course_detailForm

    class Meta:
        model = Course_detail
admin.site.register(Course_detail, Course_detailAdmin)


class Academic_detailAdmin(admin.ModelAdmin):
    list_display = ('Attendence_percentage',
                    'cname',
                    'First_year_percentage_of_marks',
                    'Second_year_percentage_of_marks',
                    'Third_year_percentage_of_marks',
                    'Fourth_year_percentage_of_marks',
                    'Total_percentage_of_marks',
                    'Class_awarded')

    class Meta:
        model = Academic_detail
admin.site.register(Academic_detail, Academic_detailAdmin)


class Miscellaneous_detailAdmin(admin.ModelAdmin):
    list_display = ('nss',
                    'ncc',
                    'sports',
                    'hobbies',
                    'personal_website',
                    'orkut_profile_url',
                    'facebook_profile_url',
                    'linkedin_profile_url')

    class Meta:
        model = Miscellaneous_detail
admin.site.register(Miscellaneous_detail, Miscellaneous_detailAdmin)
