from django.db import models
from django.contrib.gis.db import models
# Create your models here.


class PointsOfInterest(models.Model):
    name = models.CharField(max_length=60)
    # Create Point Field
    location = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='PointsOfInterest'


class Streets(models.Model):
    name = models.CharField(max_length=80)
    location = models.LineStringField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Streets'