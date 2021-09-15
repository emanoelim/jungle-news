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

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields()
        request = self.context.get('request')
        if not request.user.is_authenticated:
            fields.pop('body')
        return fields

    @staticmethod
    def get_first_paragraph(instance):
        first_paragraph = instance.body.split('</p>')[0]
        first_paragraph = first_paragraph.replace('<div>', '')
        return f'{first_paragraph}</p>'
