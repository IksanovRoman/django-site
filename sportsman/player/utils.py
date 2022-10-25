from django.db.models import Count

from .models import *

menu = [{'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'О сайте', 'url_name': 'about'},
        ]


class DataMixin:
    paginate_by = 7

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('player'))

        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
