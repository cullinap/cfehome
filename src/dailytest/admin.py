from django.contrib import admin

# Register your models here.
from .models import DailyRecord

admin.site.register(DailyRecord)