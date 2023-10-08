import django_filters

from post.models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    body = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__username')

    class Meta:
        model = Post
        fields = ['title', 'body', 'author']
