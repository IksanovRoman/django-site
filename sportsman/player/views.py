from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


# Create your views here.
def index(request):
    posts = Player.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'player/index.html', context=context)


def about(request):
    return render(request, 'player/about.html', {'menu': menu, 'title': 'О сайте'})


def add_page(request):
    return HttpResponse(f"Добавить статью")


def contact(request):
    return HttpResponse(f"Обратная связь")


def login(request):
    return HttpResponse(f"Авторизация")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с идентификатором {post_id}")


def PageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
