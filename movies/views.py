from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie
# Create your views here.


def index(request):
    """This is our first vue function"""
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_id):
    detail = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', context={
        'detail': detail
    })
