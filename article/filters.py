from django_filters.rest_framework import FilterSet, CharFilter

from article.models import Article


class ArticleFilterSet(FilterSet):
    category = CharFilter(field_name='category__name')

    class Meta:
        model = Article
        fields = ['category']
