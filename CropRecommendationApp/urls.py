from django.urls import path
from .views import *

Error_404 = 'CropRecommendationApp.views.Error_404'
Error_500 = 'CropRecommendationApp.views.Error_500'

urlpatterns = [    
    path('',Index,name='home'),

    path('Crop/',Crop,name='crop'),
    path('Crop/<str:crop_name>/',Crop_details),    

    path('Recommend/',Crop_recommend,name='crop_recommend'),    
    
    path('About-Us/',About_us,name='about_us'),
    path('Contact-Us/',Contact_us,name='contact_us'),        
]
