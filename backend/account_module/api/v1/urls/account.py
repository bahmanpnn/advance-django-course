from django.urls import path

# from rest_framework.authtoken.views import ObtainAuthToken
from .. import views


urlpatterns = [
    # http://127.0.0.1:8000/accounts/api/v1/
    # path('',views..as_view(),name=""),
    # test email sending
    path("test-email/", views.SendTestEmail.as_view(), name="email-sending-test"),
    # registration
    path("registration/", views.RegistrationApiView.as_view(), name="registeration"),
    # activation
    path(
        "activation/confirm/<str:token>",
        views.ActivationAccountAPIView.as_view(),
        name="activation-account",
    ),
    path(
        "activation/resend/",
        views.ActivationResendGenerciAPIView.as_view(),
        name="resend-activation-account",
    ),
    # reset password
    # change password
    path(
        "change-password/",
        views.CustomChangePasswordApiView.as_view(),
        name="custom-change-password",
    ),
    # login token
    # path('token/login/',ObtainAuthToken.as_view(),name="token-login"),
    # path('token/custom-login/',views.CustomObtainAuthToken.as_view(),name="custom-token-login"),
    # logout
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    # user profile
    path("profile/", views.UserProfileApiView.as_view(), name="user-profile"),
]
