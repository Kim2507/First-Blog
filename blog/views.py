from django.shortcuts import render
from rest_framework import viewsets

from blog.serializers import PostSerializer,BooksSerializer
from blog.models import Books, Post

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

def post_list(request):
  return render(request, 'blog/post_list.html', {}) 

class BooksViewSet(viewsets.ModelViewSet):
  queryset = Books.objects.all()
  serializer_class = BooksSerializer

def books_list(request):
  return render(request, 'blog/books_list.html', {}) 