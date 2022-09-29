from django.db import models



class Metering(models.Model):
    metering_code = models.CharField(max_length=255)
    date = models.DateField()
    primary_value = models.FloatField()
    type = models.CharField(max_length=255,default='Heat')
    apartment = models.CharField(max_length=255,default='a0A9K00000012qSUAQ')