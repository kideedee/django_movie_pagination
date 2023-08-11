from django.core.paginator import Paginator
from django.shortcuts import render

from newapp.models import Movie


def movie_list(request):
    movies = Movie.objects.all()

    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movies = movies.filter(name__icontains=movie_name)

    paginator = Paginator(movies, 5)
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    return render(request, 'newapp/movie_list.html', context={'movies': movies})
