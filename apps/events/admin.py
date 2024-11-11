from django.contrib import admin

from apps.events.models import Event, EventAdmin

admin.site.register(Event, EventAdmin)