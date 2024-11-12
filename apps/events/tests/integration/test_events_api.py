from django.urls import reverse
from rest_framework import status

from apps.events.models import Event
from apps.events.tests.integration.test_setup import TestEventsSetup
from project.urls import urlpatterns


class TestEventsAPI(TestEventsSetup):

    def test_get_all_events(self):

        url = reverse('getevents')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)


    def test_get_event_by_id(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('getevent', kwargs={'pk':3})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'Art Exhibition')


    def test_register_to_event(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('register', kwargs={'pk': 4})
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        event = Event.objects.get(id=4)
        self.assertEqual(event.attendees.count(), 2)


    def test_remove_from_event(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('remove', kwargs={'eventid': 5, 'userid': 4})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_remove_from_event_not_allowed(self):
        self.client.force_authenticate(user=self.regular_user)
        url = reverse('remove', kwargs={'eventid': 5, 'userid': 4})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_get_participants_by_event(self):
            self.client.force_authenticate(user=self.user)
            url = reverse('getparticipants', kwargs={'pk': 2})
            response = self.client.get(url)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data.get('attendees')), 2)


    def test_create(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('add')
        data = {
            "name": "Volleyball Meetup",
            "description": "Today is a good day for volleyball.",
            "date": "2024-10-07T05:59:40.115516Z",
            "location": "Beach Court",
            "capacity": 25,
            "organizer": "sports club",
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_not_allowed(self):
        self.client.force_authenticate(user=self.regular_user)
        url = reverse('add')
        data = {
            "name": "Volleyball Meetup",
            "description": "Today is a good day for volleyball.",
            "date": "2024-10-07T05:59:40.115516Z",
            "location": "Beach Court",
            "capacity": 25,
            "organizer": "sports club",
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('update', kwargs={'pk': 5})
        data = {
            "name": "Movie Night Under the Stars",
          "description": "Outdoor screening of classic movies.",
          "date": "2024-10-20T20:00:00Z",
          "location": "Open Air Theater",
          "capacity": 250,
          "organizer": "Outdoor Cinema Co",
        }

        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('delete', kwargs={'pk': 3})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
