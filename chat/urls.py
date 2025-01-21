 
 
from django.urls import path  
from . import views
urlpatterns = [
     
    path('',views.home,name="home"),
    path('room/<str:room_name>/',views.room,name="room"),
    path('create_rooms/',views.create_rooms,name="create_rooms")
]
