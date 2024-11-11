from django.db import models
from django.contrib import admin
# from apps.users.models import User


class Event(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=20)
    capacity = models.IntegerField()
    organizer = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    attendees = models.ManyToManyField(
        "users.User",
        related_name="attending"
    )


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date', 'location', 'capacity', 'organizer','created_at')
    fields = ('name', 'description', 'date', 'location', 'capacity', 'organizer')
