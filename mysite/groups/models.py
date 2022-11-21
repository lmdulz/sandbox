from django.db import models
from django.contrib.auth.models import Group
from mysite.models import DicomNode

class Access(models.Model):
    
      
    class AccessType(models.TextChoices):
        BIDIRECTIONAL = "bi", "Bidirectional"
        SOURCE = "src", "Source"
        DESTINATION = "dst", "Destination" 

    access_type = models.CharField(max_length=3, choices=AccessType.choices)
    
    group  = models.ForeignKey(Group,on_delete=models.CASCADE, related_name='GroupAccess')
    node   = models.ForeignKey(DicomNode, on_delete=models.CASCADE)

