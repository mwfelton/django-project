from django.contrib import admin

# Register your models here.
from .models import LandingPageEntry

class LandingPageEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']
    readonly_fields = ['name', 'email', 'timestamp', 'updated']

admin.site.register(LandingPageEntry, LandingPageEntryAdmin)