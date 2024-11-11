from rest_framework import serializers
from .models import Event
from ..users.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta :
        model = Event
        fields = ('name', 'description', 'date', 'location', 'capacity', 'organizer')


class EventAttendeesSerializer(serializers.ModelSerializer):

    attendees = UserSerializer(read_only=True, many=True)

    class Meta :
        model = Event
        fields = ('name', 'description', 'organizer', 'attendees')


