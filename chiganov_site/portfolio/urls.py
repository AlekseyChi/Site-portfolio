from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('news/', views.news, name='news'),
    path('contacts/', views.contacts, name='contacts'),
    path('users/', views.users, name='users'),
]