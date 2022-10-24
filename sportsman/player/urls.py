from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', PlayerHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', PlayerCategory.as_view(), name='category'),
]