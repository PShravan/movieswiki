from rest_framework import serializers

from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class GenreRelateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)  # "__all__"
        extra_kwargs = {
            'name': {'validators': []},
        }


class MovieListSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True) #GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "director", "popularity99_rating", "imdb_rating", "genre")
    

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreRelateSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("title", "director", "popularity99_rating", "imdb_rating", "genre")
    
    def validate_popularity99_rating(self, rating):
        if not 0.0<=rating<=100.0:
            raise serializers.ValidationError("99popularity rating should be between 0 and 100")
        return rating

    def validate_imdb_rating(self, rating):
        if not 0.0<=rating<=10.0:
            raise serializers.ValidationError("imdb rating should be between 0 and 10")
        return rating


    def create(self, validated_data):
        genre_data = validated_data.pop('genre')
        movie = Movie.objects.create(title=validated_data['title'],director=validated_data['director'],popularity99_rating=validated_data['popularity99_rating'],imdb_rating=validated_data['imdb_rating'])

        for genre in genre_data:
            obj, created = Genre.objects.get_or_create(name=genre["name"].strip())
            movie.genre.add(obj)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.director = validated_data.get('director', instance.director)
        instance.popularity99_rating = validated_data.get('created', instance.popularity99_rating)
        instance.imdb_rating = validated_data.get('imdb_rating', instance.imdb_rating)
        instance.genre.clear()

        genre_data = validated_data.pop('genre')
        for genre in genre_data:
            obj, created = Genre.objects.get_or_create(name=genre["name"].strip())
            instance.genre.add(obj)
        return instance