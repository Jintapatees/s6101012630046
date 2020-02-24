from django.db import models
from django.conf import settings

class input(models.Model):
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)
    
    def __str__(self):
        return self.x