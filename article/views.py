from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from article.filters import ArticleFilterSet
from article.serializers import ArticleSerializer, ArticleCreateSerializer
from article.models import Article


class ArticleView(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Article.objects.all()
    serializer_class = (ArticleSerializer, ArticleCreateSerializer)

    def get_serializer_class(self):
        if self.action == 'create':
            return ArticleCreateSerializer
        return ArticleSerializer


class ArticleListView(ModelViewSet):
    http_method_names = ['get']
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ArticleFilterSet
