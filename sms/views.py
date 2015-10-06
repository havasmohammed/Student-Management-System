from django.shortcuts import render

# Create your views here.
from .forms import Login_pageForm, Basic_detailForm, Course_detailForm


def loginpage(request):
    title = "LOGIN PAGE "
    print request
    form = Login_pageForm(request.POST)
    context = {
        "title": title,
        "form": form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "loginpage.html", context)


def basicdetail(request):
    title = "BASIC DETAILS"
    print request
    form = Basic_detailForm(request.POST)
    context = {
        "title": title,
        "form": form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "basicdetail.html", context)


def coursedetail(request):
    title = "COURSE DETAILS"
    print request
    form = Course_detailForm(request.POST)
    context = {
        "title": title,
        "form": form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "coursedetail.html", context)
