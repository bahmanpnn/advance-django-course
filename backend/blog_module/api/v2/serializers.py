from rest_framework import serializers
from ...models import Post,Category


# class PostSerializer(serializers.Serializer):
#     # remember that fields name must be the same name of model fields name.
#     # for example we cant change id or title name to another things like post_id or post_title.
#     id=serializers.IntegerField()
#     title=serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    """there is three type of readonly field"""
    # type 1 - readonly field
    # content=serializers.ReadOnlyField()
    # type 2 - readonly field 
    # content=serializers.CharField(read_only=True)

    class Meta:
        model=Post
        # fields="__all__"
        fields=["id","author","title","content","category","status","created_date","published_date"]

        # type 3 - readonly fields
        read_only_fields=['content']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        # fields=["id",""]
    