from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AccountViewSet, GenreViewSet, LoginViewSet, MovieViewSet

app_name = 'kmdb'
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'accounts', AccountViewSet, basename='accounts')
router.register(r'login', LoginViewSet, basename='login')

# urlpatterns = [path('movies/<int:id>/reviews', view_de_exemplo)]

urlpatterns = router.urls
