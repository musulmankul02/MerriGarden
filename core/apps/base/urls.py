from django.urls import path, include
from apps.base import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('list_price/', views.list_price, name='list_price'),
    path('news/', views.news, name = 'news'),
    path('blog_news/<int:id>/', views.blog_news, name='blog_news'),
   path('contact', views.ContactView.as_view(), name='contact')
]