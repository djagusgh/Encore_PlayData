from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Guest

# Create your views here.

def index(request):
    return render(request, 'index.html')

def writeform(request):
    return render(request, 'writeform.html')

def write(request):
    title = request.POST['title']
    content = request.POST['content']
    g = Guest(title=title, content=content)
    g.save() # 저장 
    return redirect('list')

def list(request):
    guests = Guest.objects.all().order_by('-id') # - : 역순 정렬! -> 최신 글 먼저 나오게! 
    print(guests)
    return render(request, 'list.html', {'guests':guests})
