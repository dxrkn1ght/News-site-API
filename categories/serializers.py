from .models import Category
from rest_framework import serializers
from django.utils.text import slugify


class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        validated_data['slug'] = validated_data.get('slug') or slugify(validated_data['name'])
        return super().create(validated_data)

