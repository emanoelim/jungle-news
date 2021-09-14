import uuid

from django.db import models

from author.models import Author


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title
