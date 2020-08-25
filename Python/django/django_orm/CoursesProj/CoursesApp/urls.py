from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('course/<int:id>',views.onecourse),
    path('course/<int:id>/remove',views.remove),
]
