"""post URL Configuration

Add API endpoints urls here.
"""
from django.urls import path

from post.api import views as post_api_views

urlpatterns = [
    path('', post_api_views.PostListCreateAPIView.as_view(),
        name=post_api_views.PostListCreateAPIView.name),
    path('<int:pk>/',
        post_api_views.PostRetrieveUpdateDestroyAPIView.as_view(),
        name=post_api_views.PostRetrieveUpdateDestroyAPIView.name),
    path('author/<int:author_id>/',
         post_api_views.PostByAuthorView.as_view(),
         name=post_api_views.PostByAuthorView.name),
]
