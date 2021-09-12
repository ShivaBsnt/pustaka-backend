from rest_framework.permissions import BasePermission
from client.models import Client, ClientGrant


class OauthPermission(BasePermission):
    def has_permission(self, request, view):
        client_id = request.headers.get('x-client-id')
        client_secret = request.headers.get('x-client-secret')
        access_token = request.headers.get('x-access-token')
        try:
            client = Client.objects.get(client_id=client_id, client_secret=client_secret)
        except Client.DoesNotExist:
            return False
        try:
            code = ClientGrant.objects.get(access_token=access_token, client=client)
        except ClientGrant.DoesNotExist:
            return False
        view.oauth_user = code.user
        return True

