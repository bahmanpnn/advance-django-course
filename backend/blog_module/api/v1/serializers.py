from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    # remember that fields name must be the same name of model fields name.
    # for example we cant change id or title name to another things like post_id or post_title.
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)
    