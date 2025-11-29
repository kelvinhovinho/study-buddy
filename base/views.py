from django.shortcuts import render
from .models import Room

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {"rooms":rooms}
    return render(request, 'base/home.html',context)

def room(request, pk):
    rooms = Room.objects.get(id=pk)
    return render(request, 'base/room.html',{"rooms":rooms})