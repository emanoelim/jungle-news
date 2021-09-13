from django.urls import path, include
from rest_framework.routers import DefaultRouter

from author.views import AuthorView

router = DefaultRouter()
router.register('author', AuthorView)

urlpatterns = [
    path('', include(router.urls)),
]
