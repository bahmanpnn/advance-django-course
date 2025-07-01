from django.urls import path
from . import views as v1_views


urlpatterns = [
    # http://127.0.0.1:8000/blog/api/v1/posts/
    path('posts/',v1_views.post_list_api_view,name="post-list-api-view"),
    # remember that if you dont set type of arg,django consider default string for it.
    # for example if we dont set int for detail endpoint it just get integer value for arg ==> /<id>/<int:id>
    path('posts/<int:id>/',v1_views.post_detail_api_view,name="post-detail-api-view"),
]
