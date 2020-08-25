from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('processM', views.processM),
    path('destroy',views.destroy),
]

