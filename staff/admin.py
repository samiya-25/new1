from django.contrib import admin
from .models import Staff

# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display=['title','name']

admin.site.register(Staff,StaffAdmin)    
