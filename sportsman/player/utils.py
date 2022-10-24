from django.db.models import Count

from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]

class DataMixin:
    paginate_by = 6

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('player'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context