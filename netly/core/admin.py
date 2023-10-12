from django.contrib import admin
from . models import User, Genre, Movie

# Register your models

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Movie)
