from django.urls import path,include


urlpatterns = [
    path('',include("account_module.api.v1.urls.account")),
    path('jwt/',include("account_module.api.v1.urls.jwt")),
]