from django.db import models
from django.contrib.auth.models import Group
from mysite.models import DicomNode

class Access(models.Model):
    
      
    class AccessType(models.TextChoices):
        BIDIRECTIONAL = "bi", "Bidirectional"
        SOURCE = "src", "Source"
        DESTINATION = "dst", "Destination" 

    
    access_type = models.CharField(max_length = 3, choices=AccessType.choices)
    
    group  = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='GroupAccess' )
    node   = models.ForeignKey(DicomNode, on_delete=models.CASCADE)
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
        self.name = f"{access_type_dict[self.access_type]}_{self.group}_{self.node}"
        super(Access, self).save(*args, **kwargs)
    




    #name = models.CharField(unique=False, max_length=128, null = True, blank=True, editable=False,default = f"{access_type_dict[access_type]}_{group}_{node}")
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    # # #def __str__(self):
    #     access_type_dict = dict(self.AccessType.choices)
        
    #     self.name = models.CharField(unique=False, max_length=128, null = True, blank=True, editable=False,default = f"{self.access_type}_{self.group}_{self.node.name}")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.access_type = self.access_type
    #     self.group = group
    #     self.node = node

    # access_type_dict = dict(self.AccessType.choices)
    # name = models.CharField(unique=True, max_length=128, null = True, default = f"{access_type_dict[self.node_type]}_{self.group}_{self.node}")
    
    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.name = f"{self.access_type}_{self.group}_{self.node}"
    
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