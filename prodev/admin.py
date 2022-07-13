from django.contrib import admin

from prodev.models import Time_Worked,Project,User,Reviews

# Register your models here.


admin.site.register(Time_Worked)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Reviews)
