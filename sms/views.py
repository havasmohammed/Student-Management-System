from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import LoginPageForm, BasicDetailForm, CourseDetailForm


def index(request):
    return HttpResponse("Student Information System")


def loginpage(request):
    title = "LOGIN PAGE "
    print request
    form = LoginPageForm(request.POST)
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
    form = BasicDetailForm(request.POST)
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
    form = CourseDetailForm(request.POST)
    context = {
        "title": title,
        "form": form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "coursedetail.html", context)
