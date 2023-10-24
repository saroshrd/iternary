from django.http import HttpResponse
from backend.models import City, Itinerary
from backend.serializers import CitySerializer
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render 

from .serializers import CitySerializer,  ItinerarySerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()

    def get_serializer_class(self):
        return CitySerializer

    def list(self, request, *args, **kwargs):
        movies = City.objects.all()
        serializer = CitySerializer(movies, many=True)
        return Response(serializer.data)
    

class ItineraryViewSet(viewsets.ModelViewSet):

    queryset = Itinerary.objects.all()

    def get_serializer_class(self):
        return ItinerarySerializer

    def list(self, request, *args, **kwargs):
        movies = Itinerary.objects.all()
        serializer = ItinerarySerializer(movies, many=True)
        return Response(serializer.data)
    

# create a function 
def home_screen(request): 
    # return response 
    return render(request, "t1.html") 
