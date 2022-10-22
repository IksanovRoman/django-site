from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = ['Главная страница', 'О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

# Create your views here.
def index(request):
    posts = Player.objects.all()
    return render(request, 'player/index.html', {'posts': posts, 'menu': menu, 'title':'Главная страница'})

def about(request):
    return render(request, 'player/about.html', {'menu': menu, 'title':'О сайте'})

def categories(request, catid):
    return HttpResponse(f"Категории спортсменов. Страница №{catid}")

def archive(request, year):
    return HttpResponse(f"Страница с годом {year}")

def PageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")