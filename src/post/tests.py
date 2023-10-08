from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
# from rest_framework_simplejwt.tokens import Token
from post.api import views as post_api_views
from rest_framework import status
from post.models import Post

User = get_user_model() # return active user model in project


# Create your tests here.
class PostAPITests(APITestCase):
    model = Post
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.post_data = {
            'title': 'Test Post',
            'body': 'This is a test post.',
            'author': self.user,
        }
        self.post = self.model.objects.create(**self.post_data)
    
    def test_post(self):
        url = reverse(post_api_views.PostListCreateAPIView.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.assertEqual(self.model.objects.count(), 1)
    
    def test_create_post(self):
        url = reverse(post_api_views.PostListCreateAPIView.name)
        response = self.client.post(url, self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_retrieve_post_list(self):
        url = reverse(post_api_views.PostListCreateAPIView.name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)

    def test_retrieve_post_detail(self):
        url = reverse(post_api_views.PostRetrieveUpdateDestroyAPIView.name, args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)
        self.assertEqual(response.data.get('body'), self.post.body)
        self.assertEqual(response.data.get('author', {}).get('username'), self.user.username)

    def test_update_post(self):
        updated_data = {
            'title': 'Updated Post',
            'body': 'This post has been updated.',
        }
        url = reverse(post_api_views.PostRetrieveUpdateDestroyAPIView.name, args=[self.post.id])
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, updated_data['title'])
        self.assertEqual(self.post.body, updated_data['body'])

    def test_delete_post(self):
        url = reverse(post_api_views.PostRetrieveUpdateDestroyAPIView.name, args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

