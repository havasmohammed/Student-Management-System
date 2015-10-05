from django.contrib import admin

from .models import Basic_detail, Course_detail
from .forms import Basic_detailForm, Course_detailForm


class Basic_detailAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sid', 'gender', 'address', 'DOB',
                    'father_name', 'mother_name', 'email')
    form = Basic_detailForm

    class Meta:
        model = Basic_detail
admin.site.register(Basic_detail, Basic_detailAdmin)


class Course_detailAdmin(admin.ModelAdmin):
    list_display = ('cnum', 'cname', 'credits', 'year_of_registration')
    form = Course_detailForm

    class Meta:
        model = Course_detail
admin.site.register(Course_detail, Course_detailAdmin)
