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

'''
lu = User(username="luca")
gruppen = lu.groups.get()

In [11]: gruppen
Out[11]: <Group: DIR>

In [12]: gruppen.GroupAccess.all()
Out[12]: <QuerySet [<Access: Access object (1)>]>

In [13]: gruppen.GroupAccess.filter(access_type="src")

zugang = gruppen.GroupAccess.filter(access_type="src")

In [28]: zugang.first().node.source_active
Out[28]: False
'''