from django.http import HttpResponse
from  django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, get_object_or_404
from client.models import Client, ClientGrant
from user.serializers.user import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print(request.data)
        print(request.user)
        print(kwargs['client_id'])
        client = get_object_or_404(Client, client_id=kwargs['client_id'])
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        grant, _ = ClientGrant.objects.get_or_create(client=client, user=user)
        print(grant)
        print(user)
        return Response({
            "access_token": grant.access_token,
            "redirect_url": client.redirect_url,
            "username": user.username
        })


class UserAuthenticateAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        print(kwargs['client_id'])
        print("inside custom Auth ")
        user = User.objects.get(username=request.user)
        client = get_object_or_404(Client, client_id=kwargs['client_id'])
        grant, _ = ClientGrant.objects.get_or_create(client=client, user=user)
        return Response({
            "access_token": grant.access_token,
            "redirect_url": client.redirect_url
        })


