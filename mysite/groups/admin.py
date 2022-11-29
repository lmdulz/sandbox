from django.contrib import admin
from .models import Access

class AccessAdmin(admin.ModelAdmin):
     list_display = ("name","access_type",
                     "group",
                     "node")
     
admin.site.register(Access, AccessAdmin)