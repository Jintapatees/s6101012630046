from django.db import models

class History(models.Model):
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)
    operator = models.CharField(max_length=2000,null=True)
    result = models.IntegerField(null=True)
    def __str__(self):
        return self.x