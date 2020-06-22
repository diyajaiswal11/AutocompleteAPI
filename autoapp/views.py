from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import Countries, Cities, States
import csv
import json

def search(request):
    s=request.GET['s']
    l=[]
    with open('cities.csv',encoding="utf8") as csvfile:
        citydata = list(csv.reader(csvfile))
        for row in citydata:
            if row[1].lower()==s.lower() or s.lower() in row[1].lower():
                l.append(row)
    with open('countries.csv',encoding="utf8") as csvfile:
        countrydata = list(csv.reader(csvfile))
        for row in countrydata:
            if row[1].lower()==s.lower() or s.lower() in row[1].lower():
                l.append(row)
    with open('states.csv',encoding="utf8") as csvfile:
        statesdata = list(csv.reader(csvfile))
        for row in statesdata:
            if row[1].lower()==s.lower() or s.lower() in row[1].lower():
                l.append(row)

    for obj in Countries.objects.all():
        co=[]
        if obj.name.lower()==s.lower() or s.lower() in obj.name.lower():
            co.append(obj.id)
            co.append(obj.name)
            co.append(obj.iso3)
            co.append(obj.iso2)
            co.append(obj.phone_code)
            co.append(obj.capital)
            co.append(obj.currency)
            co.append(obj.native)
            co.append(obj.emoji)
            co.append(obj.emojiU)
            l.append(co)
    #frommodel=list(Countries.objects.filter(name__icontains=s).values_list('name',flat=True))
    l1 = json.dumps(l)
    print(l1)
    #print(frommodel)
    return JsonResponse(data=l1,status=200)

