from django.db import models

class Access(models.Model):
    
      
    class AccessType(models.TextChoices):
        BIDIRECTIONAL = "bi", "Bidirectional"
        SOURCE = "src", "Source"
        DESTINATION = "dst", "Destination" 

    access_type = models.CharField(max_length=2, choices=AccessType.choices)
    
    group  = models.ForeignKey(models.Group,on_delete=models.CASCADE)
    node   = models.ForeignKey(DicomNode, on_delete=models.CASCADE)

