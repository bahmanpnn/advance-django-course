from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes,action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.views import APIView
from rest_framework import mixins,viewsets,generics,status
from django_filters.rest_framework import DjangoFilterBackend
from permissions import IsAuthorOrReadOnlyPermission
from .serializers import PostSerializer,CategorySerializer
from ...models import Post,Category # from blog_module.models import Post


# Django Rest Framework v2 Endpoints.

# version 1 ==> APIView
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

#-------------------------------------------------------------------
# version 2 ==> generic api view + mixins
# Post list view
# class PostListGenericAPIView(generics.GenericAPIView):
#     """ getting a list of posts and creating new posts."""
#     # permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class=PostSerializer
#     queryset=Post.objects.all()
    
#     def get(self,request):
#         """ retriveing a list of posts."""
#         queryset=self.get_queryset()
#         serializer=self.serializer_class(queryset,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         """creating a post with provided data."""
#         serializer=self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class PostListGenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     """ getting a list of posts and creating new posts with generic api view and list model and create model mixins."""
#     # permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class=PostSerializer
#     queryset=Post.objects.all()
    
#     # def get(self, request, *args, **kwargs):
#     #     return self.retrieve(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# Post detail view
# class PostDetailGenericAPIView(generics.GenericAPIView):
#     """ getting a detail of post object with updating or deleting that object."""
#     # permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class=PostSerializer

#     def get(self,request,pk):
#         """retrieving a post object data."""
#         post=get_object_or_404(Post,pk=pk,status=True)
#         serializer=self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         """editing a post object data."""
#         post=get_object_or_404(Post,pk=pk,status=True)
#         serializer=self.serializer_class(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,request,pk):
#         """deleting a post object."""
#         post=get_object_or_404(Post,pk=pk,status=True)
#         post.delete()
#         return Response({"detail":"post deleted successfully"},status=status.HTTP_204_NO_CONTENT) 


# class PostDetailGenericAPIView(generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     """ getting a detail of post object with updating or deleting that object."""
#     # permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class=PostSerializer
#     queryset=queryset=Post.objects.all()
#     # lookup_field='id'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


#-------------------------------------------------------------------
# 3 generics classes
# Post list view
class PostListGenericAPIView(generics.ListCreateAPIView):
    """ 
        Concrete view for listing a queryset or creating a model instance.
        getting a list of posts and creating new posts with list create api view that inheritance from ListModelMixin,CreateModelMixin and GenericAPIView
        if we need more options in class we can override methods of it and add things that we want them.
    """
    # permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    queryset=Post.objects.all()

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

# Post detail view
class PostDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ 
        getting a detail of post object with updating or deleting that object.
        if we need more options,have to override methods of that class.
    """
    # permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    queryset=queryset=Post.objects.all()
    # lookup_field='id'

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


# 4 viewsets
class PostListViewSet(viewsets.ViewSet):
    """ 
        getting a list of posts and creating new post and a detail of post object with updating or deleting that object with just one class.
        that is a combination of two views(post list and post detail) but they handles and need 2 urls to pass every method that call and need.
    """

    # permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    queryset=Post.objects.all()

    def list(self,request):
        """ retriveing a list of posts."""
        serializer=self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        """creating a post with provided data."""
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        """retrieving a post object data."""
        post=get_object_or_404(Post,pk=pk,status=True)
        serializer=self.serializer_class(post)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        """editing a post object data."""
        post=get_object_or_404(Post,pk=pk,status=True)
        serializer=self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self,request,pk=None):
        """deleting a post object."""
        post=get_object_or_404(Post,pk=pk,status=True)
        post.delete()
        return Response({"detail":"post deleted successfully"},status=status.HTTP_204_NO_CONTENT) 

    def partial_update(self,request,pk=None):
        """editing a partial of post object data like some fields of that obj and passs some of them not all of them?"""
        post=get_object_or_404(Post,pk=pk,status=True)
        serializer=self.serializer_class(post,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

# Model viewset inheritances all of CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin,GenericViewSet, 
# and does'nt need to set methods just when we need to override one of them we can write that method again.
class PostListModelViewSet(viewsets.ModelViewSet):
    """ 
        getting a list of posts and creating new post and a detail of post object with updating or deleting that object with just one class.
        that is a combination of two views(post list and post detail) but they handles and need 2 urls to pass every method that call and need.
    """
    permission_classes=[IsAuthenticatedOrReadOnly,IsAuthorOrReadOnlyPermission]
    serializer_class=PostSerializer
    queryset=Post.objects.all()

    filter_backends=[DjangoFilterBackend]
    filterset_fields=['category','author','status']
    

class CategoryListModelViewSet(viewsets.ModelViewSet):
    """ 
        getting a list of categories and creating new category and a detail of category object with updating or deleting that object with just one class.
    """

    # permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

    @action(detail=False,methods=['get'])
    def get_category_ok(self,request):
        """if we need extra method we can set a new method with action decorator to have extra method plus own viewset methods(list,retrieve,update,...)"""
        return Response({"detail":"ok"})


class CustomViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """ if we need custom viewset we can create a custom viewset with generic viewset"""
    
    pass