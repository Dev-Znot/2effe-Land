from django.db import models

class LandModel(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    whatsapp = models.CharField(max_length=16, blank=False, null=False)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
    
