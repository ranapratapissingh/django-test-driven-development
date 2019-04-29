from django.contrib import admin

from .models import Entry, Comment

# Register your models here.

admin.site.register(Entry)
admin.site.register(Comment)

