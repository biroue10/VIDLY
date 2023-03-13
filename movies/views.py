from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.


def index(request):
    """This is our first vue function"""
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
