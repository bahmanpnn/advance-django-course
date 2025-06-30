from django.urls import path
from . import views as v1_views


urlpatterns = [
    path('posts/',v1_views.post_list_api_view,name="post-list-api-view"),
]
