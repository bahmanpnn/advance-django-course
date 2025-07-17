from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from ...models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True,max_length=255)

    class Meta:
        model=User
        fields=['email','password','password2']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({'detail':'passwords doesn\'t match'})
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password2',None)
        return User.objects.create_user(**validated_data)
    
    def to_representation(self, instance):
        """
            this method is for show object data that serve with serializer and we can change way of sending data with displaying.
            remember that, another reason of using request here is using the serializer for both list and post detail endpoints and
            we want to handle both with one serializer but sometimes its better to seprate serializers and views. 
        """
        
        rep=super().to_representation(instance)
        return rep

    
    