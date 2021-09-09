from django.contrib import admin
from .models import Stuff

# Register your models here.
# class Stuff(admin.ModelAdmin):
#     list_display = ('pk', 'title', 'content', 'created_at', 'update_at',)

admin.site.register(Stuff)
