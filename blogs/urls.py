from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreate, LoginView, BlogStoriesViewSet

router = DefaultRouter()
router.register(r'blog/stories', BlogStoriesViewSet, basename='blog_stories')

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls