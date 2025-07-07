from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.views import APIView
from .serializers import PostSerializer
from ...models import Post # from blog_module.models import Post


# Django Rest Framework v2 Endpoints.

class PostListAPIView(APIView):
    """ getting a list of posts and creating new posts"""
    # permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    
    def get(self,request):
        """ retriveing a list of posts"""
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        """creating a post with provided data"""
        serializer=PostSerializer(data=request.data) # passing data arg for serializer is very important when we need checking validation.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail_api_view(request,id):
    post=get_object_or_404(Post,pk=id,status=True)
    if request.method=="GET":
        serializer=PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        # its important to know in delete design pattern we can use staus 200 too and it deponds on us to choose which one is better.but 204 is more common.
        return Response({"detail":"post deleted successfully"},status=status.HTTP_204_NO_CONTENT) 
     
