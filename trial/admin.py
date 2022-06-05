from django.contrib import admin
from .models import Contact, Trial
# Register your models here.
class TrialAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','iptv_type']

admin.site.register(Trial,TrialAdmin)
admin.site.register(Contact)