from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ...models import User, Profile


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, max_length=255)

    class Meta:
        model = User
        fields = ["email", "password", "password2"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError(
                {"detail": "passwords doesn't match"}
            )
        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password2", None)
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        """
        this method is for show object data that serve with serializer and we can change way of sending data with displaying.
        remember that, another reason of using request here is using the serializer for both list and post detail endpoints and
        we want to handle both with one serializer but sometimes its better to seprate serializers and views.
        """

        rep = super().to_representation(instance)
        return rep


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        username = attrs.get("email")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
            if not user.is_verified:
                msg = _(
                    "Your account is not verified; Unable to log without verifing account."
                )
                raise serializers.ValidationError(msg, code="authorization")

        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if not self.user.is_verified:
            msg = _(
                "Your account is not verified; Unable to log without verifing account."
            )
            raise serializers.ValidationError(msg, code="authorization")
        validated_data["email"] = self.user.email
        validated_data["user_id"] = self.user.id
        return validated_data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError(
                {
                    "detail": "new password and confirm new password don't match"
                }
            )
        try:
            validate_password(
                attrs.get("new_password")
            )  # django checks password complexity
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {"new_password": list(e.messages)}
            )

        return super().validate(attrs)


class UserProfileModelSerializer(serializers.ModelSerializer):
    # email=serializers.CharField(source='user.email') # next time override validate method of serializer to user can update its email or something like it from other models that fetch here!!
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name",
            "avatar",
            "description",
            "email",
        ]


class ActivationResendSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")

        # check user exists or not
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "user does not exist"}
            )
        if user_obj.is_verified:
            raise serializers.ValidationError(
                {"detail": "user is already activated and verified!!"}
            )
        attrs["user"] = user_obj

        return super().validate(attrs)
