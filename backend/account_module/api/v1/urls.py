from django.urls import path,include
from rest_framework.routers import DefaultRouter,SimpleRouter
from . import views

app_name="api-v1"

urlpatterns = [
    # http://127.0.0.1:8000/accounts/api/v1//

    # registration
    path('registration/',views.RegistrationApiView.as_view(),name="registeration")

    # change password

    # reset password

    # login token

    # login jwt

]



