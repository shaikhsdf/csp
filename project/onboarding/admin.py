from django.contrib import admin# Register your models here.
from .models import *

admin.site.site_header = 'Candidate Selection Portal'
admin.site.register(function)
admin.site.register(sub_function)
admin.site.register(designation)
admin.site.register(location)
admin.site.register(sub_location)
admin.site.register(state)
admin.site.register(user_group)
admin.site.register(candidate)