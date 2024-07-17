from django.db import models

# Create your models here.

class Poengliste(models.Model):
  navn = models.CharField(max_length=100)
  poeng = models.IntegerField()
