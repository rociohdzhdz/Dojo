from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('newuser', views.newuser),
    path('quotes', views.quotes),
    path('loginuser', views.loginuser),
    path('usererror', views.usererror),
    path('userexist', views.userexist),
    path('errorprofile', views.errorprofile),
    path('newquote', views.newquote),
    path('user/<int:id>', views.user),
    path('myaccount/<int:id>', views.myaccount),
    path('givelike/<int:id>', views.givelike),
    path('delete/<int:id>', views.delete),
    path('logout', views.logout),
]
