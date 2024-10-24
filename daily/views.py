from django.shortcuts import render

def index(request):
    return render(request, 'daily/index.html')

def __str__(self):
    return self.title
