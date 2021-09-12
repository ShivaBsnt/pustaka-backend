from  rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_app', 'client_id', 'redirect_url', 'client_name']
        extra_kwargs = {'client_name': {
            'read_only': True,
            'required': True
        },
            'client_id': {
                'read_only': True
            }

        }


