from django.contrib import admin
from .models import Room  # Updated to match the renamed model

admin.site.register(Room)