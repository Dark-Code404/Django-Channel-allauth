 
import os
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
 

from .forms import *

 

# Create your views here.

 

def home(request):
    rooms=Room.objects.all()

    
    context={
        "rooms":rooms, 
         
        }

    return render(request, "main.html",context)

def create_rooms(request):

    form=RoomCreate()
    if request.method=='POST':
        form=RoomCreate(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.created_by=request.user
            room.save()
            return HttpResponse("Room created successfully!")
        else:
            print(form.errors)
            return HttpResponse("form error")
        
    
        


    return render(request,"create_rooms.html",{"form":form})


def room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    messages=Message.objects.filter(room=room).order_by('timestamp')

    
    context={
        "room": room,
        "messages":messages
        }
   
    return render(request, "room.html",context)


def profile(request):
    return render(request, "profile.html",{})