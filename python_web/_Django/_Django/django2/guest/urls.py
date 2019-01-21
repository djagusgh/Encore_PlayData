# guest/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('writeform', views.writeform),
    path('write', views.write),
    path('list', views.list),
]

