# -*- coding: iso-8859-15 -*-
from django.db import models

# Create your models here.

class VehicleLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_time = models.DateTimeField('date captured')
    angle = models.FloatField(default = 0.0)

    def __str__(self):
        return '%s | (%f, %f); %0.2f°' % (self.date_time.strftime('%d/%m/%Y - %H:%M:%S'), \
                                          self.latitude, self.longitude, self.angle)

