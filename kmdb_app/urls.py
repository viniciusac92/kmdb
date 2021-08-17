from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import GenreViewSet, MovieViewSet

app_name = 'kmdb'
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
urlpatterns = router.urls
