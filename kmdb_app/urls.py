from rest_framework.routers import DefaultRouter

from .views import AccountViewSet, GenreViewSet, MovieViewSet

app_name = 'kmdb'
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
