from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from ...models import Post # from blog_module.models import Post


# Django Rest Framework v1 Endpoints.
# Post List Endpoints

# @api_view()
# def post_list_api_view(request):
#     # posts=Post.objects.all()
#     posts=Post.objects.filter(status=True)
#     serializer=PostSerializer(posts,many=True)
#     return Response(serializer.data)


# @api_view(["GET","POST"])
# def post_list_api_view(request):
#     if request.method == "GET":
#         posts=Post.objects.filter(status=True)
#         serializer=PostSerializer(posts,many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer=PostSerializer(data=request.data) # passing data arg for serializer is very important when we need checking validation.
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# more clean code for checking validation with no condition and lower code lines.
@api_view(["GET","POST"])
def post_list_api_view(request):
    if request.method == "GET":
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer=PostSerializer(data=request.data) # passing data arg for serializer is very important when we need checking validation.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Post Detail Endpoints
# @api_view()
# def post_detail_api_view(request,id):
#     try:
#         post=Post.objects.get(pk=id)
#         serializer=PostSerializer(post)
#         return Response(serializer.data)
#     except Post.DoesNotExist:
#         # remember that structure of sending data for response is a dictionary,
#         # so we have to send values and args with dictionary like detail in this example.
#         return Response({"detail":"post does'nt exists!! try again"},status=status.HTTP_404_NOT_FOUND)


# @api_view()
# def post_detail_api_view(request,id):
#     # post=get_object_or_404(Post,pk=id)
#     # add status filtering when django wants to find post object. 
#     post=get_object_or_404(Post,pk=id,status=True)
#     serializer=PostSerializer(post)
#     return Response(serializer.data)


@api_view(["GET","PUT","DELETE"])
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
     
    