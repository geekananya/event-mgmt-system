from datetime import datetime
from django.test import TestCase
from apps.events.serializers import EventSerializer, EventAttendeesSerializer

class EventSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        data = {
            'name': 'Event1',
            'description': "Some event",
            'date': datetime(2023, 10, 23),
            'location': 'City1',
            'capacity': 130,
            'organizer': 'Some org'
        }
        serializer = EventSerializer(data=data)
        self.assertTrue(serializer.is_valid())


class EventAttendeesSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        data = {
            'name': 'Event1',
            'description': "Some event",
            'organizer': 'Some org',
            'attendees': {
                'first_name': 'user21',
                'email': 'user@gamidl.com',
                'is_admin': True,
            }
        }
        serializer = EventAttendeesSerializer(data=data)
        self.assertTrue(serializer.is_valid())