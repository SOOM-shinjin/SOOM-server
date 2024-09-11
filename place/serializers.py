from rest_framework import serializers
from .models import Place, PlaceImage, Like

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class PlaceListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ['name', 'thumbnail', 'like_count', 'short_description']

    def get_thumbnail(self, obj):
        # 해당 플레이스의 사진들 중 id=1인 사진이 있으면 그 사진의 URL을 반환
        image = PlaceImage.objects.filter(place=obj).first()
        if image:
            return image.image.url
        return None

    def get_like_count(self, obj):
        return Like.objects.filter(place=obj).count()

    def get_short_description(self, obj):
        return obj.description[:20] + '...' if len(obj.description) > 20 else obj.description
