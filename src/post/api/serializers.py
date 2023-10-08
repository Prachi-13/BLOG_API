from rest_framework import serializers
from post.models import Post
from account.api.serializers import UserPublicSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'body', 'author', 'created_date', 'last_modified_date')

class PostListSerializer(serializers.ModelSerializer):
    # author = UserPublicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'body', 'author', 'created_date', 'last_modified_date')
        read_only_fields = ('author', )
