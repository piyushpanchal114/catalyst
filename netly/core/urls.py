from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register("genres", views.GenreViewSet)
router.register("movies", views.MovieViewSet)

urlpatterns = router.urls
