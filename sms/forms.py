from django import forms

from .models import Basic_detail, Course_detail, Login_page


class Login_pageForm(forms.ModelForm):
    class Meta:
        model = Login_page
        fields = ['sid', 'password']


class Basic_detailForm(forms.ModelForm):
    class Meta:
        model = Basic_detail
        fields = ['first_name', 'last_name', 'sid', 'gender', 'address', 'DOB',
                  'father_name', 'mother_name', 'email']


class Course_detailForm(forms.ModelForm):
    class Meta:
        model = Course_detail
        fields = ['cnum', 'cname', 'stream', 'credits', 'year_of_registration']
