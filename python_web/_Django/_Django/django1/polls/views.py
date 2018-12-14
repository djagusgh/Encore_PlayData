from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice

# Create your views here.

# http://127.0.0.1:8000/polls/
def index(request):
    # return HttpResponse('Hello world')
    latest_question_list = Question.objects.all()
    print(latest_question_list)

    context = {"latest_question_list" : latest_question_list}

    return render(request, 'index.html', context)

# http://127.0.0.1:8000/polls/1
def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        print(question)

        return render(request, 'detail.html', {'question' : question})

# latest_choice_list = Choice.objects.all()
# print(latest_choice_list)