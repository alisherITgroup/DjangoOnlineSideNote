from django.db import models


# Create your models here.
class Dictionary(models.Model):
    english = models.CharField(max_length=100, verbose_name="English")
    uzbek = models.CharField(max_length=100, verbose_name="Uzbek")
