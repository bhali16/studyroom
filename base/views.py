from django.shortcuts import render
from django.http import HttpResponse
from . models import Room
from . forms import RoomForm

rooms = [
    {'id':1, 'name': "Python"},
    {'id':3, 'name': "Javascript"},
    {'id':2, 'name': "Laravel"},
]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}

    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)