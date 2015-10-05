from django.shortcuts import render

# Create your views here.
from .forms import Basic_detailForm


def Basic_detail(request):
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
    return render(request, "Basic_detail.html", context)
