# polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # http://127.0.0.1:8000/polls/
    path('', views.index), # 첫 페이지
    # http://127.0.0.1:8000/polls/2
    path('<question_id>/' , views.detail), # 상세 페이지
    # http://127.0.0.1:8000/polls/2/vote/
    path('<question_id>/vote/', views.vote), # 투표
    # http://127.0.0.1:8000/polls/2/results/
    path('<question_id>/results/', views.results), # 결과
]