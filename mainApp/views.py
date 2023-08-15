from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import NameForm
from .models import Room, Message, DummyMessage
from datetime import datetime, timedelta
# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html')

def access_room(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        room_name = form.data['room_name']
        user_name = form.data['user_name']
        print(user_name)
        print(room_name)
        request.session['user_name'] = user_name
        return redirect('mainApp:room_name', room_name)
    else:
        return redirect('mainApp:index')
    
def room_name(request, room_name):
    user_name = request.session['user_name']
    print(user_name)
    now = datetime.now()
    listMsg = [
        DummyMessage("Happy Monkey", "Hello World 1", "Hippo", (now - timedelta(minutes=0)).strftime("%H:%M:%S")),
        DummyMessage("Happy Monkey", "Hello World 2", "Rhino", (now - timedelta(minutes=0)).strftime("%H:%M:%S")),
        DummyMessage("Happy Monkey", "Hello World 3", "Hippo", (now - timedelta(minutes=0)).strftime("%H:%M:%S")),
        DummyMessage("Happy Monkey", "Hello World 4", "Rhino", (now - timedelta(minutes=10)).strftime("%H:%M:%S")),
        DummyMessage("Happy Monkey", "Hello World 5", "Hippo", (now - timedelta(minutes=15)).strftime("%H:%M:%S")),
        DummyMessage("Happy Monkey", "Hello World 6", "Rhino", (now - timedelta(minutes=20)).strftime("%H:%M:%S")),
        DummyMessage("Happy Monkey", "Hello World 7", "Hippo", (now - timedelta(minutes=30)).strftime("%H:%M:%S")),
    ]
    context = {
        'room_name': room_name,
        'messages': listMsg
    }
    return render(request, 'mainApp/room.html', context)