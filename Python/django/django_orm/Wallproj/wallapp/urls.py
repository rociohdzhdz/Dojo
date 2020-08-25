from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registerus', views.registerus),
    path('loginus', views.loginus),
    path('success', views.success),
    path('createmessage', views.createmessage),
    path('profile/<int:id>', views.profile),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('addcomment/<int:id>', views.addcomment),
    path('logoutus', views.logoutus),

]