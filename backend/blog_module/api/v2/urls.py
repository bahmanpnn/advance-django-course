from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views as v2_views

app_name = "api-v2"

router = DefaultRouter()
router.register("post-viewset", v2_views.PostListViewSet, basename="post-viewset")
router.register(
    "post-model-viewset", v2_views.PostListModelViewSet, basename="post-model-viewset"
)

# remember that diffrence of default and simple router is just api-root and schema for documention that there is not in simple router.
router2 = SimpleRouter()
router2.register(
    "category", v2_views.CategoryListModelViewSet, basename="category-viewset"
)


# way 1 to add router url to urlpatterns
# urlpatterns=router.urls

urlpatterns = [
    # http://127.0.0.1:8000/blog/api/v2/posts/
    # apiview
    # path('posts/',v2_views.PostListAPIView.as_view(),name="cbv-post-list-api-view"),
    # path('posts/<int:pk>/',v2_views.PostDetailAPIView.as_view(),name="cbv-post-detail-api-view"),
    # generic api view
    # path('posts/',v2_views.PostListGenericAPIView.as_view(),name="cbv-post-list-api-view"),
    # path('posts/<int:pk>/',v2_views.PostDetailGenericAPIView.as_view(),name="cbv-post-detail-api-view"),
    # viewset
    path(
        "posts/",
        v2_views.PostListViewSet.as_view({"get": "list", "post": "create"}),
        name="cbv-viewset-post-list-api-view",
    ),
    path(
        "posts/<int:pk>/",
        v2_views.PostListViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
        name="cbv-viewset-post-detail-api-view",
    ),
    # way 2 to add router url to urlpatterns
    path("post-viewset/", include(router.urls)),
    path("caregory-model-viewset/", include(router2.urls)),
]

# way 3 to add router url to urlpatterns
# urlpatterns+=router.urls
