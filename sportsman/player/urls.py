from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', PlayerHome.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', PlayerCategory.as_view(), name='category'),
]