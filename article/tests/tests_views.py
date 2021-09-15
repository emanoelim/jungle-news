from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from rest_framework.test import APIRequestFactory, force_authenticate

from article.models import Article
from article.views import ArticleListView


class TestsArticleListView(TestCase):
    def _request(self):
        article_list_view = ArticleListView.as_view({'get': 'list'})
        response = article_list_view(self.request)
        return response

    def setUp(self):
        self.factory = APIRequestFactory()
        self.request = self.factory.get('/api/articles/')
        self.user = mommy.make(User)
        mommy.make(
            Article,
            body='<div><p>First paragraph</p><p>Second paragraph</p><p>Third paragraph</p></div>'
        )

    def test_return_body_field_authenticated_user(self):
        force_authenticate(self.request, user=self.user)
        response = self._request()
        article = response.data[0]
        keys = article.keys()
        self.assertIn('body', keys)

    def test_skip_body_field_not_authenticated_user(self):
        response = self._request()
        article = response.data[0]
        keys = article.keys()
        self.assertNotIn('body', keys)

    def test_show_first_paragraph(self):
        response = self._request()
        article = response.data[0]
        first_paragraph = article.get('first_paragraph')
        self.assertEqual(first_paragraph, '<p>First paragraph</p>')
