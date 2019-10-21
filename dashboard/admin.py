from django.contrib import admin
from .models import *

class HabitsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Habits._meta.fields]

    class Meta:
        model = Habits


admin.site.register(Habits, HabitsAdmin)
