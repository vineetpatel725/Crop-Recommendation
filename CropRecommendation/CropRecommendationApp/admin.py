from django.contrib import admin
from CropRecommendationApp.models import *

# Register your models here.

admin.site.register(crop)
admin.site.register(crop_recommed)

admin.site.site_header = 'Agrikol'
admin.site.site_title = 'Agrikol'
admin.site.index_title = 'Administrator'