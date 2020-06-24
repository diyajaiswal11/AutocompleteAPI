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
    if list(request.GET)[0]=='s':
        s=request.GET['s']
        q1 = Cities.objects.filter(name__icontains=s)
        q2 = States.objects.filter(name__icontains=s)
        q3 = Countries.objects.filter(name__icontains=s)
        serializer1=CitiesSerializer(q1,many=True)
        serializer2=StatesSerializer(q2,many=True)
        serializer3=CountriesSerializer(q3,many=True)
        response={"cities":serializer1.data,
                    "states":serializer2.data,
                    "countries":serializer3.data }
    elif list(request.GET)[0]=='city':
        city=request.GET['city']
        q1 = Cities.objects.filter(name__icontains=city)
        serializer1=CitiesSerializer(q1,many=True)
        response={"cities":serializer1.data }
    elif list(request.GET)[0]=='state':
        state=request.GET['state']
        q1 = States.objects.filter(name__icontains=state)
        serializer2=StatesSerializer(q1,many=True)
        response={ "states":serializer2.data }
    elif list(request.GET)[0]=='country':
        country=request.GET['country']
        q1 = Countries.objects.filter(name__icontains=country)
        serializer3=CountriesSerializer(q1,many=True)
        response={ "countries":serializer3.data }
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