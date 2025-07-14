from rest_framework import serializers
from ...models import Post,Category
from account_module.models import Profile


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
        fields=["id","author","image","title","content","category","status","created_date","published_date","snippet","relative_url",'abs_url']

        # type 3 - readonly fields
        read_only_fields=['content','author']


    def get_abs_url(self,obj):
        """
        this method get request dictionary and add object.pk after request url==>/blog/api/v2/modelviewset/obj.pk
        *** remember that it works just for model serializer,if we use for simple serializer it raise none type error!!
        """
        req = self.context.get("request")
        return req.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        """
            this method is for show object data that serve with serializer and we can change way of sending data with displaying.
            remember that, another reason of using request here is using the serializer for both list and post detail endpoints and
            we want to handle both with one serializer but sometimes its better to seprate serializers and views. 
        """
        
        rep=super().to_representation(instance)

        request=self.context.get('request')
        # print(request.__dict__)

        rep['state']='list'
        if request.parser_context.get('kwargs').get('pk'):
            rep['state']='single object(post)'
            rep.pop('snippet',None)
            rep.pop('relative_url',None)
            rep.pop('abs_url',None)
        else:
            rep.pop('content',None)

        # rep['category']=CategorySerializer(instance.category).data # this method(to representation) is the best way to connect another serializers
        
        # if we want to use another serializer in serializer must send request for it too. 
        # sometimes we another serialzer need request to give somethings like full path(abs_url in post serializer) 
        # and for it we need to pass request here.
        # without it category serializer just return relative path for field that it have like image.
        rep['category']=CategorySerializer(instance.category,context={"request":request}).data 


        return rep

    def create(self, validated_data):
        """here we set auhtor auto and doesnt need to send fill it in post mehtod."""
        # remember that if we seperate request with  validated_data field we will have 2 query to database.so we have to consider queries in project to.
        # request=self.context.get('request')
        # validated_data['author']=Profile.object.get(user__id=request.user.id)
                
        validated_data['author']=Profile.object.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    