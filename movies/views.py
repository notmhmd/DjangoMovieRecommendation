from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .recommendation import get_similar_movies
from rest_framework.pagination import PageNumberPagination
import requests

# Create your views here.
class MovieList(APIView):
    """
    List All movies
    """
    def get(self, request, format=None):
        movies = Movie.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

class MovieDetail(APIView):
    """
     retrive movie instance
    """
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        similar_movies = get_similar_movies(movie.title)
        serializer = MovieSerializer(movie)
        return Response({"movie": serializer.data, "similar": similar_movies})
