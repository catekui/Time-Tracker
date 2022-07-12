from django.contrib import admin

from prodev.models import Time_Worked, User,Project

# Register your models here.


admin.site.register(Time_Worked)
admin.site.register(User)
admin.site.register(Project)