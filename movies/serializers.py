from rest_framework import serializers
from rest_framework.response import Response
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'plot', 'cast', 'director', 'added_on', 'url', 'poster', 'backdrop_img']
