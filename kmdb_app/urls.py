from rest_framework.routers import DefaultRouter

from .views import (
    AccountViewSet,
    GenreViewSet,
    LoginViewSet,
    MovieViewSet,
    ReviewViewSet,
)

app_name = 'kmdb'
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'accounts', AccountViewSet, basename='accounts')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'reviews', ReviewViewSet)


urlpatterns = router.urls
