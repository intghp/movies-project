from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView)

from .forms import MovieForm
from .models import MovieModel
# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse("Home!")

class MovieListView(ListView):
    model = MovieModel
    template_name = 'movies/list_movies.html'
    context_object_name = 'movies'
    
class MovieCreateView(CreateView):
    model = MovieModel
    form_class = MovieForm
    template_name = 'movies/create_movie.html'
    success_url = reverse_lazy('list_movies')

class MovieUpdateView(UpdateView):
    model = MovieModel
    form_class = MovieForm
    template_name = 'movies/update_movie.html'
    success_url = reverse_lazy('list_movies')
    
class MovieDeleteView(DeleteView):
    model = MovieModel
    template_name = 'movies/delete_movie.html'
    context_object_name = 'movie'
    success_url = reverse_lazy('list_movies')