from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from author.serializers import AuthorSerializer
from author.models import Author


class AuthorView(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
