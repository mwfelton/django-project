from django.http import HttpResponse

def home_page(*args, **kwargs):
    return HttpResponse("<h1>PISS</h1>")
