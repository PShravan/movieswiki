from django.urls import path
from .views import *

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genres-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
    path('movies/', MovieListCreateView.as_view(), name='movies-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
]
