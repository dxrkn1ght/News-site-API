from rest_framework import serializers
from .models import New, Comment


class CommentSerializer(serializers.ModelSerializer):
    new = serializers.PrimaryKeyRelatedField(queryset=New.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'
