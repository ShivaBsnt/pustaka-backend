from django.urls import path, include
from user.views.register import UserRegisterView
from user.views.logout import UserLogoutView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet
router = DefaultRouter()
router.register('', UserViewSet, basename='user')
from .views.user import UserAPIView

urlpatterns = [

    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', views.obtain_auth_token, name='login'),
    path('logout/', UserLogoutView, name='logout'),
    path('validate/', UserAPIView.as_view(), name='user')

] + router.urls
