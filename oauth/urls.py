from django.urls import path, include
# from .views import ClientLoginView
from .views import CustomAuthToken, UserAuthenticateAPI
urlpatterns = [
    path('authenticate/<uuid:client_id>/', CustomAuthToken.as_view(), name='oauth_login'),
    path('authenticate/token/<uuid:client_id>/', UserAuthenticateAPI.as_view(), name="access_token_validation")

]
