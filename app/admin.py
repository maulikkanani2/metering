from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Metering)
class MeteringAdmin(admin.ModelAdmin):
    list_display = ['metering_code','date','primary_value','type','apartment']
    
# admin.site.unregister(Group)