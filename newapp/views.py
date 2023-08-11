from django.core.paginator import Paginator
from django.shortcuts import render

from newapp.models import Movie


def movie_list(request):
    movies = Movie.objects.all()

    paginator = Paginator(movies, 1)
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    return render(request, 'newapp/movie_list.html', context={'movies': movies})
