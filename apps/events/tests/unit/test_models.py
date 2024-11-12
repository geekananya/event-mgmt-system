from datetime import datetime

from rest_framework.test import APITestCase
from apps.events.models import Event


class TestEventModel(APITestCase):

    def setUp(self):
        self.event1 = Event.objects.create(
            name='Some Event',
            date=datetime(2023, 10, 23),
            location='City1',
            capacity=130,
            organizer='Some org'
        )


    def test_valid_fields(self):
        self.assertEqual(self.event1.description, "")

    def test_default_attendees(self):
        self.assertEqual(self.event1.attendees.count(), 0)