
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createbooks',views.createbooks),
    path('one_book/<int:id>', views.one_book),
]