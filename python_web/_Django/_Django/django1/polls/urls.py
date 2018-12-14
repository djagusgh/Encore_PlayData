from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/polls/
    path('', views.index),
    # http://127.0.0.1:8000/polls/1
    path('<int:question_id>', views.detail),
]