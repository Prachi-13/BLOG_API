"""Class based view for post"""
from post.models import Post
from post.api.serializers import PostSerializer, PostListSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from framework.permissions import IsOwnerOrSuperuserOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from post.api.filters import PostFilter



class PostListCreateAPIView(ListCreateAPIView):
    """Post api endpoints."""
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    name = 'post-list'
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadOnly]
    name = 'post-detail'
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class PostByAuthorView(ListAPIView):
    serializer_class = PostSerializer
    model = Post
    name = 'author-posts'
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        return self.model.objects.filter(author__id=author_id)
