from django.db import models



# Create your models here.
class postmodel(models.Model):
    NamePost = models.CharField(max_length = 100)
    TextPost = models.CharField(max_length = 2000)

    ConfirmId = models.CharField(max_length = 15)

    def __str__(self):
        return self.ConfirmId