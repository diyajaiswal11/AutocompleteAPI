from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import Countries, Cities, States
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .serializers import CountriesSerializer,CitiesSerializer,StatesSerializer
import csv
import json




def search(request):
    s=request.GET['s']
    response=[]
    q1 = Cities.objects.filter(name__icontains=s)
    q2 = States.objects.filter(name__icontains=s)
    q3 = Countries.objects.filter(name__icontains=s)
    response.append(list(q1.values()))
    response.append(list(q2.values()))
    response.append(list(q3.values()))
    
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