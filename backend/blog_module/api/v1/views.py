from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post # from blog_module.models import Post

# Django Rest Framework v1 Endpoints.
@api_view()
def post_list_api_view(request):
    return Response("post list api view")


# @api_view()
# def post_detail_api_view(request,id):
#     data={
#         "name":"bahman",
#         "age":26,
#         "id":id
#     }
#     return Response(data)

@api_view()
def post_detail_api_view(request,id):
    post=Post.objects.get(pk=id)
    serializer=PostSerializer(post)
    return Response(serializer.data)