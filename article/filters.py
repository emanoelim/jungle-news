from django_filters.rest_framework import FilterSet, CharFilter

from article.models import Article


def _title_contains(queryset, name, value):
    return queryset.filter(title__icontains=value)


class ArticleFilterSet(FilterSet):
    category = CharFilter(field_name='category__name')
    author = CharFilter(field_name='author__name')
    title = CharFilter(field_name='title', method=_title_contains)

    class Meta:
        model = Article
        fields = ['category', 'author', 'title']
