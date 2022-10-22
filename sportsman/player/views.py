from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница")

def categories(request, catid):
    return HttpResponse(f"Категории спортсменов. Страница №{catid}")

def archive(request, year):
    return HttpResponse(f"Страница с годом {year}")

def PageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")