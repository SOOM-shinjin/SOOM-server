from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .models import Place
from .serializers import *

class PlaceFilter(filters.FilterSet):
    type = filters.MultipleChoiceFilter(field_name='type', choices=Place.TYPE_CHOICES)

    class Meta:
        model = Place
        fields = ['type']

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    filterset_class = PlaceFilter
    filter_backends = [DjangoFilterBackend]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PlaceListSerializer
        return PlaceSerializer

#     # 모든 Place 정보를 불러오는 API
#     def list(self, request):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

# class PlaceTypeViewSet(viewsets.ModelViewSet):
#     serializer_class = PlaceSerializer

#     def get_queryset(self):
#         return Place.objects.filter(type=self.type_value)

#     # '가볼 만한 곳' 필터링 API
#     def get_hot_places(self, request):
#         self.type_value = '가볼 만한 곳'
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     # '음식점' 필터링 API
#     def get_restaurants(self, request):
#         self.type_value = '음식점'
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     # '숙소' 필터링 API
#     def get_accommodations(self, request):
#         self.type_value = '숙소'
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
