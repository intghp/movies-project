from django.urls import path
from .views import (
    HomeView,
    MovieListView,
    MovieCreateView,
    MovieDeleteView,
    MovieUpdateView)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('list/', MovieListView.as_view(), name='list_movies'),
    path('create/', MovieCreateView.as_view(), name='create_movie'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='update_movie'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='delete_movie'),
]