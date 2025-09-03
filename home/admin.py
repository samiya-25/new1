from django.contrib import admin
from .models import Home
from .models import About

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display=['title','info']

class AboutAdmin(admin.ModelAdmin):
    list_display=['name','age']

admin.site.register(Home,HomeAdmin)
admin.site.register(About,AboutAdmin)