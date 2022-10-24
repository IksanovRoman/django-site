from django.contrib import admin

from .models import *


# Register your models here.
class PlayerConfig(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'photo', 'time_created', 'time_update')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_created', )
    prepopulated_fields = {'slug': ("title",) }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(Player, PlayerConfig)
admin.site.register(Category, CategoryAdmin)
