from django.conf.urls import url
from . import views

urlpatterns = [
    url('checkout', views.checkout),
    url('buy',views.buy),
    url('', views.index),
]