from django.urls import path,include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views


app_name="api-v1"

urlpatterns = [
    # http://127.0.0.1:8000/accounts/api/v1/

    # registration
    path('registration/',views.RegistrationApiView.as_view(),name="registeration"),

    # change password

    # reset password

    # login token
    path('token/login/',ObtainAuthToken.as_view(),name="token-login"),
    path('token/custom-login/',views.CustomObtainAuthToken.as_view(),name="custom-token-login"),

    #logout
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name="token-logout"),

    # login jwt
    path('jwt/create/',TokenObtainPairView.as_view(),name="jwt-create"), # pass username and password
    path('jwt/refresh/',TokenRefreshView.as_view(),name="jwt-refresh"), # pass refresh token to get access token(refresh has longer time than access token)
    path('jwt/verify/',TokenVerifyView.as_view(),name="jwt-verify"), # pass access token to verify user token and prove token didnt expire

]



