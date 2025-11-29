from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'lets learn python'},
    {'id':2, 'name':'lets learn JAVA'},
    {'id':3, 'name':'lets learn PHP'},
    {'id':4, 'name':'lets learn CSS'},
    {'id':5, 'name':'lets learn JavaScript'},
]

context = {"rooms":rooms}

def home(request):
    return render(request, 'base/home.html',context)

def room(request):
    return render(request, 'base/room.html',context)