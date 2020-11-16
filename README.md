# wikimovies project

Wikimovies is a django RESTful api for retrieving the movies data from database.
check the [link](https://movieswiki.herokuapp.com/) deployed on heroku.

## setup venv

```sh
python3 -m venv venv
source venv/bin/activate
```

## install requirements

```bash
pip install -r requirements.txt

```

## running django management commands & usage

```sh
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=movieswiki.settings
python manage.py makemigrations
python manage.py migrate
python manage.py load_movie_data
python manage.py runserver
```

# api endpoints

### User Registration

/rest-auth/registration/ (POST)

- username
- password1
- password2
- email

### Login

/rest-auth/login/ (POST)

- username
- email
- password

### Logout

/rest-auth/logout/ (POST)

### Password change

/rest-auth/password/change/ (POST)

- new_password1
- new_password2
- old_password

### obtain auth token

/api/api-auth-token/ (POST)

- username
- password

### movies list

/api/movies/ (GET)

### filter movies list

/api/movies/?search=key (GET)

### movie detail

/api/movies/<int:pk>/ (GET)

### Genres list

/api/genres/ (GET)

### Genre detail

/api/genres/<int:pk>/ (GET)

## ADMIN ONLY TASKS

### add Movie

/api/movies/ (POST)

- title
- director
- popularity99_rating
- imdb_rating
- genre (list of objects with name as attribute)
  eg: [{
  "name": "Horror"
  },
  {
  "name": "Thriller"
  }]

### update movie detail

/api/movies/<int:pk>/ (PUT)

- title
- director
- popularity99_rating
- imdb_rating
- genre (list of objects with name as attribute)
  eg: [{
  "name": "Horror"
  },
  {
  "name": "Thriller"
  }]

### delete movie

/api/movies/<int:pk>/ (DELETE)

### add genre

/api/genres/ (POST)

- name

### update genre detail

/api/genres/<int:pk>/ (PUT)

- name

### delete genre

/api/genres/<int:pk>/ (DELETE)
