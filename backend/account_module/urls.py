from django.urls import path,include


app_name='account_module'
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('api/v1/',include("account_module.api.v1.urls")),
    path('api/v2/',include("djoser.urls")),
    path('api/v2/',include("djoser.urls.jwt")),
]
