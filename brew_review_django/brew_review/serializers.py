from rest_framework import serializers
from .models import Brewery, Review

class BrewerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brewery
        fields = ('name', 'city', 'state', 'description', 'website_url',)

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('brewery', 'atmosphere', 'beer_tenders', 'beer_selection', 'notes', 'photo',)