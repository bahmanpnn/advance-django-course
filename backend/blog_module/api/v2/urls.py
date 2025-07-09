from django.urls import path
from . import views as v2_views


urlpatterns = [
    # http://127.0.0.1:8000/blog/api/v2/posts/
    # path('posts/',v2_views.PostListAPIView.as_view(),name="cbv-post-list-api-view"),
    # path('posts/<int:pk>/',v2_views.PostDetailAPIView.as_view(),name="cbv-post-detail-api-view"),

    path('posts/',v2_views.PostListGenericAPIView.as_view(),name="cbv-post-list-api-view"),
    path('posts/<int:pk>/',v2_views.PostDetailGenericAPIView.as_view(),name="cbv-post-detail-api-view"),
]
