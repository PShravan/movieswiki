from django.shortcuts import redirect
from rest_framework import filters, generics

from .models import Genre, Movie
from .permissions import IsAdminUserOrReadOnly
from .serializers import GenreSerializer, MovieListSerializer, MovieSerializer

def home(request):
    return redirect('movies-list')


class GenreListCreateView(generics.ListCreateAPIView):
    """Provides tags list to view and Allow admin to create new genre instances or others to read."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    search_fields = ["name"]
    filter_backends = (filters.SearchFilter,)


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Provides *RUD functionality for an genre instance to admin or others to read."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    """Provides tags list to view and Allow admin to create movie instances or others to read."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    search_fields = ["title", "director", "genre__name"]
    filter_backends = (filters.SearchFilter,)
    # method_serializer_classes = {
    #     ('GET', ): MovieListSerializer,
    #     ('POST'): MovieSerializer
    # }

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListSerializer
        if self.request.method == 'POST':
            return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Provides *RUD functionality for an movie instance to admin or others to read."""

    queryset = Movie.objects.all()
    # serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListSerializer
        elif self.request.method == 'PATCH' or 'PUT':
            return MovieSerializer