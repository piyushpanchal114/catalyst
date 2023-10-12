from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer, UpdateMovieSerializer


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related("genre").all()
    # serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return UpdateMovieSerializer
        elif self.request.method == "POST":
            return UpdateMovieSerializer
        else:
            return MovieSerializer
