from django.db import models
from core.models import BaseImage

class Place(models.Model):
    name = models.CharField(max_length=30)
    TYPE_CHOICES=(
        ('가볼 만한 곳','가볼 만한 곳'),
        ('음식점','음식점'),
        ('숙소','숙소'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.CharField(max_length=4000)
    location = models.CharField(max_length=1000)
    contact = models.CharField(max_length=15)
    closed_days = models.CharField(max_length=100)
    parking_facilities = models.CharField(max_length=100)
    POSSIBLE_CHOICES=(
        ('없음','없음'),
        ('가능','가능'),
        ('있음','있음'),
    )
    rent_stroller = models.CharField(max_length=10, choices=POSSIBLE_CHOICES)
    accompany_pets = models.CharField(max_length=10, choices=POSSIBLE_CHOICES)
    is_credit_card_possible = models.CharField(max_length=10, choices=POSSIBLE_CHOICES)
    admission_fee = models.CharField(max_length=200)
    is_restroom = models.CharField(max_length=10, choices=POSSIBLE_CHOICES)
    
class Like(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='likes')
    key = models.CharField(
        max_length=10,
        blank=True,
        editable=False
    )
    
    def __str__(self):
        return f'{self.place}/{self.key}'
    
class PlaceImage(BaseImage):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='placeimages')