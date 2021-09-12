from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from pustaka.serializer import DynamicFieldsModelSerializer
User = get_user_model()


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'is_active']
