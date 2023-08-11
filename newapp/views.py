from django.shortcuts import render

from newapp.models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'newapp/movie_list.html', context={'movies': movies})
