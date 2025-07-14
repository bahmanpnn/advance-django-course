from rest_framework import serializers
from ...models import Post,Category


# class PostSerializer(serializers.Serializer):
#     # remember that fields name must be the same name of model fields name.
#     # for example we cant change id or title name to another things like post_id or post_title.
#     id=serializers.IntegerField()
#     title=serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        # fields=["id",""]
    

class PostSerializer(serializers.ModelSerializer):
    """there is three type of readonly field"""
    # type 1 - readonly field
    # content=serializers.ReadOnlyField()
    # type 2 - readonly field 
    # content=serializers.CharField(read_only=True)
    
    snippet=serializers.ReadOnlyField(source='get_snippet')
    relative_url=serializers.URLField(source='get_absolute_api_url',read_only=True)
    abs_url=serializers.SerializerMethodField(method_name='get_abs_url') # with this field django search method in serializer.if dont set method name it search by default (get_)+ field name.
    
    # category=CategorySerializer()
    # category=serializers.SlugRelatedField(many=False,read_only=True,slug_field='name')
    # category=serializers.SlugRelatedField(many=False,read_only=False,slug_field='name',queryset=Category.objects.all())

    class Meta:
        model=Post
        # fields="__all__"
        fields=["id","author","title","content","category","status","created_date","published_date","snippet","relative_url",'abs_url']

        # type 3 - readonly fields
        read_only_fields=['content']

    def get_abs_url(self,obj):
        """
        this method get request dictionary and add object.pk after request url==>/blog/api/v2/modelviewset/obj.pk
        *** remember that it works just for model serializer,if we use for simple serializer it raise none type error!!
        """
        req = self.context.get("request")
        return req.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        """this method is for show object data that serve with serializer and we can change way of sending data with displaying"""
        rep=super().to_representation(instance)
        rep['category']=CategorySerializer(instance.category).data
        rep.pop('snippet',None)
        return rep

 
