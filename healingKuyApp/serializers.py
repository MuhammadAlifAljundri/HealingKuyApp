from rest_framework import serializers
from .models import Location, Bus, Schedule, Booking

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields='__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'