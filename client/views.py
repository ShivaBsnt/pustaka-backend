from pustaka.viewsets import ListCreateUpdateModelMixin
from .serializer import ClientSerializer
from .models import Client
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ClientViewSet(ListCreateUpdateModelMixin):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        self.perform_create(ser)
        return Response({
            "message": "client has been successfully created",
            "data": ser.data
        }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(client_name=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = Client.objects.filter(client_name=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


