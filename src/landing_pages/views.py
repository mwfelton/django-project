from django.shortcuts import render

# from django.http import HttpResponse
from django.shortcuts import render
from .models import LandingPageEntry
from .forms import LandingPageEntryModelForm

def home_page(request, *args, **kwargs):
    title = "Welcome Burger"
    form = LandingPageEntryModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        print(obj)
    
        form = LandingPageEntryModelForm()
        
    context = {
        "title": title,
        "form": form
    }
    # parag = "{title} Justin!".format(**context)
    return render(request, "landing_pages/home.html", context)
