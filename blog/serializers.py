from rest_framework import serializers
from blog.models import Post,Books
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('author', 'title', 'text', 'created_date', 'published_date')
    
class BooksSerializer(serializers.ModelSerializer):
  class Meta:   
    model = Books
    fields = ('ISBN','title','genre','author','published_date')