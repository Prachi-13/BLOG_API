"""Model for post"""
from framework.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings


class Post(AbstractBaseModel):
    """Post of the connect application.
         Write schema below.
    """
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        app_label = 'post'
        db_table = 'post'
        ordering = ('-created_date', )