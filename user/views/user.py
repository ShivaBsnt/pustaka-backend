from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from pustaka.viewsets import ListRetrieveUpdateModelMixin
from ..serializers.user import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from pustaka.permissions import OauthPermission
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


class UserViewSet(ListRetrieveUpdateModelMixin):
    serializer_class = UserSerializer
    oauth_user = None

    def get_queryset(self):
        if self.action in ['update', 'partial_update']:
            return User.objects.filter(id=self.request.user.id)
        return User.objects.all()

    def get_permissions(self):
        if self.action == 'oauth_retrieve':
            return [OauthPermission()]
        return super().get_permissions()

    @action(detail=False, url_path='oauth-retrieve')
    def oauth_retrieve(self, *args, **kwargs):
        serializer = self.get_serializer(self.oauth_user, fields=['username', 'first_name', 'last_name', 'email'])
        return Response(serializer.data)


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        obj = User.objects.get(username=request.user)
        serializer = UserSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)





