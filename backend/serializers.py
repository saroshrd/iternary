from rest_framework import serializers
from .models import City, Itinerary

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'description')


class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ('id', 'city', 'day', 'itinerary')