from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('city', views.CityViewSet, basename='city')
router.register('itinerary', views.ItineraryViewSet, basename='itinerary')
urlpatterns = router.urls

urlpatterns = [
    # path("backend/", views.index, name="index"),
    path('api/', include(router.urls)),
    path('home/', views.home_screen, name = "home_screen"), 
]