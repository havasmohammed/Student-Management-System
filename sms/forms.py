from django import forms

from .models import BasicDetail, CourseDetail, LoginPage, AcademicDetail, MiscellaneousDetail


class LoginPageForm(forms.ModelForm):
    class Meta:
        model = LoginPage
        fields = ['sid', 'password']


class BasicDetailForm(forms.ModelForm):
    class Meta:
        model = BasicDetail
        fields = ['first_name', 'middle_name', 'last_name', 'sid', 'gender', 'address', 'DOB',
                  'father_name', 'mother_name', 'email', 'blood_group', 'father_profession',
                  'family_income', 'religion', 'caste', 'reservation_category',
                  'emergency_contact_number']


class CourseDetailForm(forms.ModelForm):
    class Meta:
        model = CourseDetail
        fields = ['cname', 'stream', 'code', 'year_of_registration', 'duration', 'level']


class AcademicDetailForm(forms.ModelForm):
    class Meta:
        model = AcademicDetail
        fields = ['attendence_percentage',
                  # 'cname',
                  'first_year_percentage_of_marks',
                  'second_year_percentage_of_marks',
                  'third_year_percentage_of_marks',
                  'fourth_year_percentage_of_marks',
                  'total_percentage_of_marks',
                  'class_awarded']


class MiscellaneousDetailForm(forms.ModelForm):
    class Meta:
        model = MiscellaneousDetail
        fields = ['nss', 'ncc', 'sports', 'hobbies', 'personal_website', 'orkut_profile_url',
                  'facebook_profile_url', 'linkedin_profile_url']
