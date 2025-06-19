from django.contrib import admin

# Register your models here.

from .models import Question

admin.site.register(Question)



admin.site.site_header = "My Custom Admin"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to the Admin Area"
