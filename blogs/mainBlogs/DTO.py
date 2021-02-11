from rest_framework import serializers

from .models import Blog, Category


class CategoryDTO(serializers.ModelSerializer):

    id = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = ['id', 'name']


class BlogDTO(serializers.ModelSerializer):

    category = CategoryDTO(many=False)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'text', 'date_created', 'category']

