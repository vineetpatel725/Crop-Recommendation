from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
import numpy as np
import pickle as p


#-------------------------------Home---------------------------------
def Index(request):    
    recent_recommend = crop_recommed.objects.filter().order_by('-cr_id')[:4]    
    print(recent_recommend)    
    return render(request,'index.html',{'recent_recommend':recent_recommend})


#-------------------------------Crop---------------------------------
def Crop(request):
    crops = crop.objects.all()    
    return render(request,'crop.html',{"crops":crops})

def Crop_details(request,crop_name):  
    crop_details = crop.objects.get(crop_name = crop_name)    
    return render(request,'crop_details.html',{"crop_details":crop_details})


#-------------------------------Recommendation---------------------------------
def Crop_recommend(request):       
    model,accuracy = Recommendation('Crop_Recommendation.pkl')     
    if(request.POST):
        result = predict_data(model,request)                
        result_crop_data = crop.objects.get(crop_name = result.cr_crop)
        print(result_crop_data.crop_image)
        return render(request,'crop_recommend_view.html',{'result':result,'result_crop_data':result_crop_data})            
    return render(request,'crop_recommend.html',{"accuracy":accuracy})


#-------------------------------About & Contact---------------------------------
def About_us(request):
    return render(request,'about-us.html')

def Contact_us(request):
    return render(request,'contact-us.html')


#-------------------------------Recommendation Model---------------------------------
def Recommendation(recommend_file):    
    pickle_file = open('CropRecommendationApp/Model/'+recommend_file,'rb')
    model,accuracy = p.load(pickle_file)
    return model,accuracy


#-------------------------------404 Error---------------------------------
def Error_404(request,exception):    
    return render(request,'404.html')


#-------------------------------500 Error---------------------------------
def Error_500(request,exception):    
    return render(request,'500.html')


def predict_data(model,request):                
    farmer_name,soil_nitrogen,soil_phosphorous,soil_potassium = str(request.POST['farmer_name']),int(request.POST['soil_nitrogen']),int(request.POST['soil_phosphorous']),int(request.POST['soil_potassium'])
    soil_temperature,relative_humidity,soil_ph,rainfall = float(request.POST['soil_temperature']),float(request.POST['relative_humidity']),float(request.POST['soil_ph']),float(request.POST['rainfall'])
    try:            
          data = crop_recommed.objects.get(cr_nitrogen=soil_nitrogen,cr_phosphorous=soil_phosphorous,cr_potassium=soil_potassium,cr_ph=soil_ph,cr_temperature=soil_temperature,cr_humidity=relative_humidity,cr_rainfall=rainfall)        

    except crop_recommed.DoesNotExist:    
        predict_details = [soil_nitrogen,soil_phosphorous,soil_potassium,soil_temperature,relative_humidity,soil_ph,rainfall]   
        recommend_crop = model.predict(np.array([predict_details]))            
        data = crop_recommed(cr_farmername=farmer_name,cr_nitrogen=soil_nitrogen,cr_phosphorous=soil_phosphorous,cr_potassium=soil_potassium,cr_ph=soil_ph,cr_temperature=soil_temperature,cr_humidity=relative_humidity,cr_rainfall=rainfall,cr_crop=recommend_crop[0])
        data.save()    
            
    return data


#-------------------------------Admin---------------------------------
def Admin(request):    
    return render(request,'agrikol/admin/signin.html')