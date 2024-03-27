from django.contrib import admin
from .models import About, Experience, Professional, Education, Messages

# Register your models here.

admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Professional)
admin.site.register(Education)
admin.site.register(Messages)

