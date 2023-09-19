from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1, 'name': "Python"},
    {'id':3, 'name': "Javascript"},
    {'id':2, 'name': "Laravel"},
]

def home(request):
    return render(request, 'base/home.html')

def room(request):
    context = {'rooms':rooms}
    return render(request, 'base/room.html', context)