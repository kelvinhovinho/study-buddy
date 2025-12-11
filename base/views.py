from django.shortcuts import render, redirect
from .models import Room, Topic
from django.db.models import Q
from .forms import RoomForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def loginPage(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('base:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base:home')
        
        else:
            messages.error(request, "Usename or password does not exist.")



    context ={
        "page":page
        }
    return render(request, 'base/login_register.html', context)

def lougoutUser(request):
    logout(request)
    return redirect('base:home')


def registerPage(request):
    form = UserCreationForm()
    return render(request, 'base/login_register.html', {"form":form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    room_cout = rooms.count()
    topics = Topic.objects.all

    context = {
        "rooms":rooms,
        "topics":topics,
        "room_cout":room_cout
        }
    return render(request, 'base/home.html',context)

def room(request, pk):
    rooms = Room.objects.get(id=pk)
    return render(request, 'base/room.html',{"rooms":rooms})


@login_required(login_url='base:login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')


    context = {"form":form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='base:login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("Permission denied")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {"form":form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='base:login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Permission Denied")
    

    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request, 'base/delete.html', {"obj":room})