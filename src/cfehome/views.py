# from django.http import HttpResponse
from django.shortcuts import render
from .forms import LandingPageForm

def home_page(request, *args, **kwargs):
    title = "Welcome Burger"
    form = LandingPageForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = LandingPageForm()
        
    context = {
        "title": title,
        "form": form
    }
    # parag = "{title} Justin!".format(**context)
    return render(request, "home.html", context)

def abc_page(request, *args, **kwargs):
    title = "ABC"
    context = {
        "title": title
    }
    # parag = "{title} Justin!".format(**context)
    return render(request, "home.html", context)