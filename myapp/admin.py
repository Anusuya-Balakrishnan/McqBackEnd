from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import CustomUser


admin.site.register(LogEntry)

admin.site.register(CustomUser)
# Register your models here.
