import json

import django
from django.core.management.base import BaseCommand, CommandError
from movies.models import Genre, Movie

django.setup()

def populate_movies():
    print("\npopulating movies...\n")
    with open('imdb_movies.json', 'r') as f:
        data = json.load(f)
    
    for movie in data:
        print("adding: "+movie['name'])
        movie_obj = Movie.objects.create(title=movie['name'],director=movie['director'],popularity99_rating=movie['99popularity'],imdb_rating=movie['imdb_score'])
        for genre in movie["genre"]:
            genre_obj, created = Genre.objects.get_or_create(name=genre.strip())
            movie_obj.genre.add(genre_obj)
    print("Done")


class Command(BaseCommand):
    help = "loads the movies data into the models"

    def handle(self, *args, **options):
        print("\npopulating movies date in database...")
        print("\ndeleting all previous data...")
        Movie.objects.all().delete()
        Genre.objects.all().delete()
        print("Deletion Done\n\n")
        populate_movies()