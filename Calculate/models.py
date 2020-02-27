from django.db import models

class History(models.Model):
    x = models.CharField(max_length=20, null=True)
    y = models.CharField(max_length=20, null=True)
    operator = models.CharField(max_length=2,null=True)
    result = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.x + self.operator + self.y