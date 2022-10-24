from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *


# Create your views here.
class PlayerHome(DataMixin, ListView):
    model = Player
    template_name = 'player/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


# def index(request):
#     posts = Player.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'player/index.html', context=context)


def about(request):
    return render(request, 'player/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'player/add_page.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     return render(request, 'player/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse(f"Обратная связь")


def login(request):
    return HttpResponse(f"Авторизация")


class ShowPost(DataMixin, DetailView):
    model = Player
    template_name = 'player/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


#
# def show_post(request, post_slug):
#     post = get_object_or_404(Player, slug=post_slug)
#     cats = Category.objects.all()
#
#     context = {
#         'post': post,
#         'cats': cats,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'player/post.html', context=context)

class PlayerCategory(DataMixin, ListView):
    model = Player
    template_name = 'player/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected = context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Player.objects.filter(cat__slug=self.kwargs['cat_slug'])


# def show_category(request, cat_id):
#     posts = Player.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'player/index.html', context=context)


def PageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
