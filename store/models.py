from django.db import models


class Coffee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    farm = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    profile = models.CharField(max_length=200, blank=True, null=True)
    roast = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

