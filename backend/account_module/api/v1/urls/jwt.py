from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .. import views


urlpatterns = [
    # http://127.0.0.1:8000/accounts/api/v1/
    # path('',views..as_view(),name=""),
    # login jwt
    path(
        "create/", TokenObtainPairView.as_view(), name="jwt-create"
    ),  # pass username and password
    path(
        "refresh/", TokenRefreshView.as_view(), name="jwt-refresh"
    ),  # pass refresh token to get access token(refresh has longer time than access token)
    path(
        "verify/", TokenVerifyView.as_view(), name="jwt-verify"
    ),  # pass access token to verify user token and prove token didnt expire
    # custom jwt endpoints
    path(
        "custom-create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-custom-create",
    ),  # pass username and password
]
