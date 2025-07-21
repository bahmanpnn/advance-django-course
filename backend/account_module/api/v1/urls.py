from django.urls import path,include
from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework.authtoken.views import ObtainAuthToken
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
    path('token/logout/',views.CustomDiscardAuthToken.as_view().as_view(),name="token-logout"),

    # login jwt

]



