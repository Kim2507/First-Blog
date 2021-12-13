from django.urls import include, path
from rest_framework import routers
from . import views
from blog.views import PostViewSet,BooksViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'books',BooksViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('', views.post_list, name='post_list'),
  path('',views.books_list,name='books_list'),
  
]
