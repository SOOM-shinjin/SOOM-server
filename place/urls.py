from django.urls import include, path
from rest_framework import routers
from .views import *

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("", PlaceViewSet, basename="places")

type_router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path("", include(default_router.urls)),
    # path('hot-places', PlaceTypeViewSet.as_view({'get': 'get_hot_places'}), name='hot-places'),
    # path('restaurants', PlaceTypeViewSet.as_view({'get': 'get_restaurants'}), name='restaurants'),
    # path('accommodations', PlaceTypeViewSet.as_view({'get': 'get_accommodations'}), name='accommodations'),
]
