from django.contrib import admin
from .models import DicomServer, DicomFolder




class DicomServerAdmin(admin.ModelAdmin):
    list_display = ("name", "ae_title", "host", "port", "source_active", "destination_active","node_type",)



admin.site.register(DicomServer, DicomServerAdmin)


class DicomFolderAdmin(admin.ModelAdmin):
    list_display = ("name", "path", "source_active", "destination_active","node_type",)
    

admin.site.register(DicomFolder, DicomFolderAdmin)
#admin.site.register(admin.ModelAdmin)