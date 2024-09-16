from rest_framework import serializers
from .models import Place, PlaceImage, PlaceLike

class PlaceImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
        
    class Meta:
        model = PlaceImage
        fields = ['image']


class PlaceSerializer(serializers.ModelSerializer):
    placeimages = PlaceImageSerializer(many=True, required=False)
        
    def get_images(self, instance):
        request=self.context.get('request')
        placeimage=instance.placeimages.all().order_by('id')
        try:
            booth_image_serializer=PlaceImageSerializer(placeimage, many=True)
            outcome = []
            for data in booth_image_serializer.data:
                image_url = request.build_absolute_uri(data["image"])
                outcome.append(image_url)
            return outcome
        
        except:
            return None
    
        
    class Meta:
        model = Place
        fields = '__all__'

class PlaceListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()

    def get_thumbnail(self, instance):
        request = self.context.get('request')
        first_image = instance.placeimages.first()
        if first_image:
            thumbnail_url = request.build_absolute_uri(first_image.image.url)
            return thumbnail_url
        return None
    
    def get_like_count(self, obj):
        return PlaceLike.objects.filter(place=obj).count()

    def get_short_description(self, obj):
        return obj.description[:20] + '...' if len(obj.description) > 20 else obj.description
    
    class Meta:
        model = Place
        fields = ['id', 'name', 'thumbnail', 'like_count', 'short_description']

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlaceLike
        fields = [
                    'id',
                    'place', 
                    'key'
                ]
