from django.contrib import admin
from post.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'author']
    list_filter = []
    search_fields = ['title', 'body']
    