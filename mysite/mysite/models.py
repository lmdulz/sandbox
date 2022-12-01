from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from groups.models import Access


class DicomNode(models.Model):
    NODE_TYPE = None

    class NodeType(models.TextChoices):
        SERVER = "SV", "Server"
        FOLDER = "FO", "Folder"

    class Meta:
        ordering = ("name",)

    node_type = models.CharField(max_length=2, choices=NodeType.choices)
    name = models.CharField(unique=True, max_length=64)
    source_active = models.BooleanField(default=False)
    destination_active = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.node_type:
            if not self.NODE_TYPE in dict(self.NodeType.choices):
                raise AssertionError(f"Invalid node type: {self.NODE_TYPE}")
            self.node_type = self.NODE_TYPE

    def __str__(self):
        node_types_dict = dict(self.NodeType.choices)
        return f"DICOM {node_types_dict[self.node_type]} {self.name}"

   

        '''
        MAKE ALL OF THIS A SIGNAL
        https://stackoverflow.com/questions/26379026/resolving-circular-imports-in-celery-and-django
        '''
        
        # elif DicomServer.source_active == False and DicomServer.destination_active == True:
        #     Access.objects.create(
        #         access_type="dst",
        #         node = self.DicomServer
        #         )
        #     super(DicomServer, self).save(*args, **kwargs)
        # elif DicomServer.source_active == True and DicomServer.destination_active == True:
        #     Access.objects.create(
        #         access_type="bi",
        #         node = self.DicomServer
        #         )
        #     super(DicomServer, self).save(*args, **kwargs)
        # else:
        #     print("did not work")
        #     super(DicomDicomServerNode, self).save(*args, **kwargs)
    


class DicomServer(DicomNode):
    NODE_TYPE = DicomNode.NodeType.SERVER

    # traditional DICOM support
    ae_title = models.CharField(unique=True, max_length=16)
    host = models.CharField(max_length=255)
    port = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(65535)]
    )
    patient_root_find_support = models.BooleanField(default=False)
    patient_root_get_support = models.BooleanField(default=False)
    patient_root_move_support = models.BooleanField(default=False)
    study_root_find_support = models.BooleanField(default=False)
    study_root_get_support = models.BooleanField(default=False)
    study_root_move_support = models.BooleanField(default=False)
    store_scp_support = models.BooleanField(default=False)

    # (optional) DICOMweb support
    dicomweb_root_url = models.CharField(blank=True, max_length=2000)
    dicomweb_qido_support = models.BooleanField(default=False)
    dicomweb_wado_support = models.BooleanField(default=False)
    dicomweb_stow_support = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(DicomServer, self).save(*args, **kwargs)
        if self.source_active == True and self.destination_active == False:
            print("created src access")  
            
            Access.objects.create(
                access_type="src",
                node = self
            )
                           
        elif self.source_active == False and self.destination_active == True:
            Access.objects.create(
                access_type="dst",
                node = self
                )
            
        elif self.source_active == True and self.destination_active == True:
            # Access.objects.create(
            #     access_type="bi",
            #     node = self
            #     )
            Access.objects.create(
                access_type="dst",
                node = self
                )
            Access.objects.create(
                access_type="src",
                node = self
            )
            
        else:
            print("did not work")
            
    

class DicomFolder(DicomNode):
    NODE_TYPE = DicomNode.NodeType.FOLDER

    path = models.CharField(max_length=256)
    quota = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="The disk quota of this folder in GB.",
    )
    warn_size = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="When to warn the admins by Email (used space in GB).",
    )

    def save(self, *args, **kwargs):
        super(DicomServer, self).save(*args, **kwargs)
        if self.source_active == True and self.destination_active == False:
            pass
            # print("created src access")  
            
            # Access.objects.create(
            #     access_type="src",
            #     node = self
            # )
                           
        elif self.source_active == False and self.destination_active == True:
            Access.objects.create(
                access_type="dst",
                node = self
                )
            
        elif self.source_active == True and self.destination_active == True:
            # Access.objects.create(
            #     access_type="bi",
            #     node = self
            #     )
            Access.objects.create(
                access_type="dst",
                node = self
                )
            # Access.objects.create(
            #     access_type="src",
            #     node = self
            # )
            
        else:
            print("did not work")