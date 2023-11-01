from django.urls import path
from . import views

urlpatterns = [
    # the path for our index view 
    path('', views.index),
]
