from django.db import models
from django.contrib.auth.models import Group
#from mysite.models import DicomNode
from django.core.exceptions import ValidationError
from django.contrib import messages

class Access(models.Model):
    
      
    class AccessType(models.TextChoices):
        BIDIRECTIONAL = "bi", "Bidirectional"
        SOURCE = "src", "Source"
        DESTINATION = "dst", "Destination" 

    
    access_type = models.CharField(max_length = 3, choices=AccessType.choices, editable = False)
    
    group  = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='GroupAccess',null = True, blank=True,default = None, editable = False )
    node   = models.ForeignKey("mysite.DicomNode", on_delete=models.CASCADE, editable = False )
    name = models.CharField(unique=False, max_length=128, null = True, blank=True, editable=False)


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.access_type == "src" and self.node.source_active == False:
    #         raise AssertionError(f"Invalid Access type: {self.access_type}")

    #     if self.access_type == "dst" and self.node.destination_active == False:
    #         raise AssertionError(f"Invalid Access type: {self.access_type}")

    #     if self.access_type == "bi" and (self.node.destination_active == False or self.node.source_active == False):
    #         raise AssertionError(f"Invalid Access type: {self.access_type}")
            


    def save(self, *args, **kwargs):
        access_type_dict = dict(self.AccessType.choices)
        if self.access_type == "src" and self.node.source_active == False:
            raise ValidationError(f"Invalid Access type: {self.access_type}")

        if self.access_type == "dst" and self.node.destination_active == False:
            #messages.error(request, "Invalid Access Type")
            raise ValidationError(f"Invalid Access type: {self.access_type}")

        if self.access_type == "bi" and (self.node.destination_active == False or self.node.source_active == False):
            raise ValidationError(f"Invalid Access type: {self.access_type}")

        if not self.group == None:
            self.name = f"{access_type_dict[self.access_type]}_{self.group}_{self.node}"
        else:
            self.name = f"{access_type_dict[self.access_type]}_{self.node}"
        super(Access, self).save(*args, **kwargs)
    



    
'''
from accounts.models import User
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