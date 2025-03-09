from rest_framework import serializers
from .models import New, Category, Tag
from django.utils.text import slugify


class NewSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = New
        fields = '__all__'
        extra_kwargs = {
            'slug': {'read_only': True}
        }


