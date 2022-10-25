from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.
class PlayerConfig(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'time_created', 'time_update')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_created', )
    prepopulated_fields = {'slug': ("title",)}
    fields = ('title', 'slug', 'content', 'photo', 'get_html_photo', 'cat', 'time_created', 'time_update')
    readonly_fields = ('get_html_photo', 'time_created', 'time_update')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(Player, PlayerConfig)
admin.site.register(Category, CategoryAdmin)
