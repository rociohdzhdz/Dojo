from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/newshow',views.newshow),
    path('createshow',views.createshow),
    path('shows',views.shows),
    path('shows/<int:id>',views.one_show),
    path('shows/<int:id>/edit',views.editshow),
    path('shows/<int:id>/updateshow',views.updateshow),
    path('shows/<int:id>/destroyshow',views.destroyshow),
]