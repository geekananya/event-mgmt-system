from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    path('get', views.get_events, name='getevents'),
    path('get/<int:pk>', views.get_event_by_id, name='getevent'),
    path('participants/<int:pk>', views.get_event_participants, name='getparticipants'),
    path('create', views.create, name='add'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('register/<int:pk>', views.register, name='register'),
    path('remove/<int:eventid>/<int:userid>', views.remove_user, name='remove'),
]