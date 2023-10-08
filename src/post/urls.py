"""post URL Configuration

Add API endpoints urls here.
"""
from django.urls import path

from post.views import PostView

routing_table_without_id = {

    "GET": "get_all_posts",
    "POST": "create_post"
}
routing_table_with_id = {
    "GET": "get_single_post",
    "PUT": "update_post"
}

urlpatterns = [
    path(
        '',
        PostView.as_view(
            routing_table=routing_table_without_id),
        name='post'),
    path(
        '/<resource_id>',
        PostView.as_view(
            routing_table=routing_table_with_id),
        name='post-id')]
