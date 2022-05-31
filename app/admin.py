from django.contrib import admin

# Register your models here.
from .models import Entry, Blog

admin.site.register(Entry)
admin.site.register(Blog)
