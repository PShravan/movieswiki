from django.test import TestCase
from .models import Genre, Movie

# Create your tests here.


class TestModels(TestCase):
    def test_movie_has_a_genre(self):
        movie = Movie.objects.create(title="The Conjuring", director="James Wan")
        horror = Genre.objects.create(name="Horror")
        thriller = Genre.objects.create(name="Thriller")
        horror.movie_set.add(movie)
        thriller.movie_set.add(movie)
        self.assertEqual(movie.genre.count(), 2)

    def test_movie_rating_in_bounds(self):
        movie = Movie.objects.create(
            title="The Conjuring", director="James Wan", imdb_rating=17.5
        )

    def test_post_movie(self):
        data = {
            "title": "The Conjuring",
            "director": "James Wan",
            "genre": ["Horror", "Thriller"],
            "popularity99_rating": 99,
            "imdb_rating": 9.0
        }
        response = self.client.post("/api/movies/", data=data)
        print(response)
        self.assertEqual(Movie.objects.count(), 1)
        
