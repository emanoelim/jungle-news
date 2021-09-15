from django.urls import path, include
from rest_framework.routers import DefaultRouter

from article.views import ArticleView, ArticleListView

router = DefaultRouter()
router.register('admin/articles', ArticleView)
router.register('articles', ArticleListView)

urlpatterns = [
    path('', include(router.urls)),
]
