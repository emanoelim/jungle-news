from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="Jugle News API",
        default_version='v1',
        contact=openapi.Contact(email="emanoeli.madalosso@gmail.com"),
    ),
    public=True,
)

urlpatterns = [
    path('swagger.<slug:format>)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('author.urls')),
    path('', include('article.urls')),
    path('', include('authentication.urls')),
]
