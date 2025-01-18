from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message  # Use PascalCase to import the models

@login_required
def rooms(request):
    rooms = Room.objects.all()  # Use the corrected class name
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room_instance = Room.objects.get(slug=slug)  # Rename variable to avoid shadowing the function name
    messages = Message.objects.filter(room=room_instance)[0:25]  # Use the corrected model name
    return render(request, 'room/room.html', {'room': room_instance, 'messages': messages})
