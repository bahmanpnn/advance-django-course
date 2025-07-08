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
    """ getting a list of posts and creating new posts."""
    # permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    
    def get(self,request):
        """ retriveing a list of posts."""
        posts=Post.objects.filter(status=True)
        serializer=self.serializer_class(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        """creating a post with provided data."""
        serializer=self.serializer_class(data=request.data) # passing data arg for serializer is very important when we need checking validation.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
   

class PostDetailAPIView(APIView):
    """ getting a detail of post object with updating or deleting that object."""
    # permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer

    def get(self,request,pk):
        """retrieving a post object data."""
        post=get_object_or_404(Post,pk=pk,status=True)
        serializer=self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,pk):
        """editing a post object data."""
        post=get_object_or_404(Post,pk=pk,status=True)
        serializer=self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        """deleting a post object."""
        post=get_object_or_404(Post,pk=pk,status=True)
        post.delete()
        return Response({"detail":"post deleted successfully"},status=status.HTTP_204_NO_CONTENT) 