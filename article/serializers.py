from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    first_paragraph = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        depth = 1

    @staticmethod
    def get_first_paragraph(instance):
        return instance.body.split('.')[0]
