from django.contrib import admin
from .models import *


class DestinationAdmin(admin.ModelAdmin):
    search_fields = ['full_name','destinatio']
    pass

class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Destinations, DestinationAdmin)
admin.site.register(Services, ServiceAdmin)