from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('logistique/', views.logistics, name='logistics'),
    path('articles/', views.articles, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('devis/', views.quote, name='quote'),
    path('contact/', views.contact, name='contact'),
]

