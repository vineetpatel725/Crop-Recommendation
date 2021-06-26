from django.db import models
from django.db.models.fields import *

# Create your models here.

class crop(models.Model):
    crop_id = models.AutoField('Crop ID',primary_key=True)
    crop_name = models.CharField('Crop Name',max_length=100,unique=True)
    crop_details = models.TextField('Crop Details',max_length=400)
    crop_category = models.CharField('Crop Category',max_length=20)
    crop_image = models.ImageField('Crop Image',upload_to='upload_images/crop/')

    def __str__(self):
        return self.crop_name


class crop_recommed(models.Model):
    cr_id = models.AutoField('Crop Recommend ID',primary_key=True)
    cr_farmername = models.CharField('Farmer Name',max_length=100)
    cr_nitrogen = models.PositiveIntegerField('Soil Nitrogen')
    cr_phosphorous = models.PositiveIntegerField('Soil Phosphorous')
    cr_potassium = models.PositiveIntegerField('Soil Potassium')
    cr_ph = models.FloatField('Soil ph',max_length=100)
    cr_temperature = models.FloatField('Soil Temperature',max_length=100)
    cr_humidity = models.FloatField('Relative Humidity',max_length=100)
    cr_rainfall = models.FloatField('Rainfall',max_length=100)
    cr_crop = models.CharField('Recommended Crop',max_length=100)
    
