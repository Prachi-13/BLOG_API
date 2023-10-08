"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import generics
from rest_framework.reverse import reverse

from rest_framework.response import Response

from framework.api import views as framework_api_views
from account.api import views as account_api_views
from post.api import views as post_api_views

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, format=None, **kwargs):
        return Response({
            'health_check': reverse(framework_api_views.APIHealthCheck.name, request=request, format=format),
            'posts': reverse(post_api_views.PostListCreateAPIView.name, request=request, format=format),
            'users': reverse(account_api_views.UserListAPIView.name, request=request, format=format),
            'user_register': reverse(account_api_views.UserRegisterAPIView.name, request=request, format=format),
            # 'swagger_endpoints': reverse('schema-swagger-ui', request=request, format=format),
       })


api_urlpatterns = [
        path('api/', include([
            path('', ApiRoot.as_view(), name=ApiRoot.name),
            path('account/', include('account.api.urls')),
            path('post/', include('post.api.urls')),
            path('health/', framework_api_views.APIHealthCheck.as_view(), name=framework_api_views.APIHealthCheck.name),
            # path('swagger/', schema_view.with_ui(
            #     'swagger', cache_timeout=0), name='schema-swagger-ui'),
        ]
    )),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += api_urlpatterns
