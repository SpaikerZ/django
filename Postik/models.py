from django.db import models
from django.utils.timezone import now
import datetime
from datetime import datetime

# Create your models here.
class postmodel(models.Model):
    id = models.AutoField(primary_key=True)
    NamePost = models.CharField(max_length = 100)
    TextPost = models.CharField(max_length = 2000)
    ConfirmId = models.CharField(max_length = 15)
    DatePost = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.ConfirmId
        return self.NamePost
        return self.TextPost

class confirmmodel(models.Model):
    ConfirmId = models.CharField(max_length = 15)

    def __str__(self):
        return self.ConfirmId