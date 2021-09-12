from django.db import models
from django.contrib.auth.models import User
import uuid
from pustaka.models import TimeStampModel


class Client(TimeStampModel):
    client_app = models.CharField(max_length=120)
    client_id = models.UUIDField(default=uuid.uuid4)
    client_secret = models.UUIDField(default=uuid.uuid4)
    redirect_url = models.CharField(max_length=120)

    def __str__(self):
        return self.client_app


class ClientGrant(TimeStampModel):
    access_token = models.UUIDField(default=uuid.uuid4)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
