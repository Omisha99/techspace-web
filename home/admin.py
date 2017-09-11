from django.contrib import admin
from .models import Contact, Club, Association 
# Register your models here.
admin.site.register(Contact, list_display=['name', 'email','content','app_name'])
admin.site.register(Club)
admin.site.register(Association)