from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('newdojo', views.newdojo),
    path('newninja', views.newninja),
]
