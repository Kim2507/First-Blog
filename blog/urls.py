from django.urls import include, path
from rest_framework import routers
from . import views
from blog.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('', views.post_list, name='post_list'),
]