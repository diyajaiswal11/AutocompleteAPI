from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import Countries, Cities, States
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import CountriesSerializer,CitiesSerializer,StatesSerializer
import csv
import json



def search(request):
    s=request.GET['s']
    response=[]
    with open('cities.csv',encoding="utf8") as csvfile:
        citydata = list(csv.reader(csvfile))
        for row in citydata:
            if row[1].lower()==s.lower() or s.lower() in row[1].lower():
                res={"id":row[0],"name":row[1],"state_id":row[2],"state_code":row[3],"country_id":row[4],
                "country_code":row[5],"latitude":row[6],"longitude":row[7]}
                response.append(res.copy())
                
    with open('countries.csv',encoding="utf8") as csvfile:
        countrydata = list(csv.reader(csvfile))
        for row in countrydata:
            if row[1].lower()==s.lower() or s.lower() in row[1].lower():
                res={"id":row[0],"name":row[1],"iso3":row[2],"iso2":row[3],"phone_code":row[4],"capital":row[5],
                "currency":row[6],"native":row[7],"emoji":row[8],"emojiU":row[9]}
                response.append(res.copy())

    with open('states.csv',encoding="utf8") as csvfile:
        statesdata = list(csv.reader(csvfile))
        for row in statesdata:
            if row[1].lower()==s.lower() or s.lower() in row[1].lower():
                res={"id":row[0],"name":row[1],"country_id":row[2],"country_code":row[3],"state_code":row[4]}
                response.append(res.copy())

    for obj in Countries.objects.all():
        if obj.name.lower()==s.lower() or s.lower() in obj.name.lower():
            res={"id":obj.i_d,"name":obj.name,"iso3":obj.iso3,"iso2":obj.iso2,"phone_code":obj.phone_code,
            "capital":obj.capital,"currency":obj.currency,"native":obj.native,"emoji":obj.emoji,"emojiU":obj.emojiU}
            response.append(res.copy())
            
    for obj in States.objects.all():
        if obj.name.lower()==s.lower() or s.lower() in obj.name.lower():
            res={"id":obj.i_d,"name":obj.name,"country_id":obj.country_id,"country_code":obj.country_code,"state_code":obj.state_code}
            response.append(res.copy())
            
    for obj in Cities.objects.all():
        if obj.name.lower()==s.lower() or s.lower() in obj.name.lower():
            res={"id":obj.i_d,"name":obj.name,"state_id":obj.state_id,"state_code":obj.state_code,"country_id":obj.country_id,
                "country_code":obj.country_code,"latitude":obj.latitude,"longitude":obj.longitude}
            response.append(res.copy())
            
    
    return JsonResponse(data=response,status=200,safe=False)



@csrf_exempt
def addlocation(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        if len(data)==8:
            serializer=CitiesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status=201)
        elif len(data)==10:
            serializer=CountriesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status=201)
        elif len(data)==5:
            serializer=StatesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.errors,status=400)