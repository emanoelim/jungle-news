from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from authentication.serializers import SignUpSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
