from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Place
from .serializers import PlaceSerializer, PlaceListSerializer

class PlaceViewSet(viewsets.GenericViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # 모든 Place 정보를 불러오는 API
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PlaceTypeViewSet(viewsets.GenericViewSet):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.filter(type=self.type_value)

    # '가볼 만한 곳' 필터링 API
    def get_hot_places(self, request):
        self.type_value = '가볼 만한 곳'
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # '음식점' 필터링 API
    def get_restaurants(self, request):
        self.type_value = '음식점'
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # '숙소' 필터링 API
    def get_accommodations(self, request):
        self.type_value = '숙소'
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
