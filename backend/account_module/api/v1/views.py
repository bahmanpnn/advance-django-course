from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer,CustomAuthTokenSerializer


class RegistrationApiView(generics.GenericAPIView):
    serializer_class=RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # way 1
            # serializer.validated_data.pop('password')
            # serializer.validated_data.pop('password2')
            # return Response(serializer.validated_data,status=status.HTTP_201_CREATED)

            # *** i dont know why it doesnt work!! check it later
            # way 2
            # serializer.data.pop('email')
            # print(serializer.data)

            # return Response(serializer.data,status=status.HTTP_201_CREATED)

            # way 3
            data={
                'email':serializer.validated_data['email']
            }
            return Response(data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class=CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id':user.pk,
            'email':user.email
            })
    



