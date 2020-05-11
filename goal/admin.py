from django.contrib import admin

# Register your models here.
from goal.models import Goal, GoalTransaction

admin.site.register(Goal)
admin.site.register(GoalTransaction)
