from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response


def home(request):
    return HttpResponse('hello')


def cities(request):
    import csv
    with open('cities.csv',encoding="utf8") as csvfile:
        data = list(csv.reader(csvfile))
        #print(data)
        for row in data:
            name=row[1]
            if name=='Qala i Naw':
                print("1")
                break
        
    return HttpResponse("hello")