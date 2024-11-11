from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from .models import Event
from .serializers import EventSerializer, EventAttendeesSerializer
from ..users.models import User
from permissions import IsAdmin


@api_view(['GET'])
def home(request):
    return Response({'msg':'Welcome to event mgmt system'})


@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    return Response(EventSerializer(events, many=True).data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_event_by_id(request, pk):
    event = get_object_or_404(Event, id=pk)
    serializer = EventSerializer(event)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdmin])
def get_event_participants(request, pk):
    event = get_object_or_404(Event, id=pk)
    serializer = EventAttendeesSerializer(event)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdmin])
def create(request):

    serializer = EventSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return success response
    else:
        return Response({"error": serializer.errors})


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdmin])
def update(request, pk):
    event = Event.objects.get(id=pk)

    serializer = EventSerializer(instance=event, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdmin])
def delete(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event)
    event.delete()
    return Response(serializer.data)


# register to event
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def register(request, pk):
    user = User.objects.get(email=request.user)
    event = Event.objects.get(id=pk)
    event.attendees.add(user)
    event.save()
    # check in user model also (reverse relations)
    return Response({'msg': 'success'}, status=HTTP_200_OK)


# remove users from events
@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdmin])
def remove_user(request, eventid, userid):
    user = User.objects.get(id=userid)
    event = Event.objects.get(id=eventid)
    event.attendees.remove(user)
    event.save()
    return Response({'msg': 'success'}, status=HTTP_200_OK)