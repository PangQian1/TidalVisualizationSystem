from django.db import models

# Create your models here.
class GridAttr(models.Model):
    gridNum = models.BigIntegerField(default=0, primary_key = True)
    x_coor = models.BigIntegerField(default=0)
    y_coor = models.BigIntegerField(default=0)
    longi = models.FloatField()
    lati = models.FloatField()
    road_name = models.CharField(max_length=50)

class DateGrid(models.Model):
    gridNum = models.BigIntegerField(default=0)
    date = models.DateField()

class GirdSplice(models.Model):
    startCoor = models.CharField(max_length=100)
    endCoor = models.CharField(max_length=100)
    length = models.BigIntegerField(default=0)
    name = models.CharField(max_length=500)
    date = models.DateField()