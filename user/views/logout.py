from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class UserLogoutView(APIView):
    print("we are here")
    http_method_names = ['delete']

    def delete(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({
            "message": "user has been successfully logged out",
        }, status=status.HTTP_200_OK)
