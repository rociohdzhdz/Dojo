from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registerus', views.registerus),
    path('loginus', views.loginus),
    path('success', views.success),
    path('logoutus', views.logoutus)
]