from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserRegistrationAPIView


urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="user-registration"),
    path("login/", obtain_auth_token, name = "user-obtain-auth-token")
]