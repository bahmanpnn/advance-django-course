# from django.core.mail import send_mail # django default email sending
from mail_templated import send_mail # mail templated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import ( TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView
                                         )
from .serializers import (RegistrationSerializer,
                            CustomAuthTokenSerializer,
                            CustomTokenObtainPairSerializer,
                            ChangePasswordSerializer,
                            UserProfileModelSerializer
                            )
from ...models import Profile

User=get_user_model()


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


# class CustomObtainAuthToken(ObtainAuthToken):
#     serializer_class=CustomAuthTokenSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id':user.pk,
#             'email':user.email
#             })
    

class CustomDiscardAuthToken(APIView):
    """
        we use APIView because it doesnt need serializer for get or post methods.so just apiview doesnt need serializer in drf views.
    """
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        request.user.auth_token.delete()
        # in front we can handle it and redirect user to homepage or something
        return Response(status=status.HTTP_204_NO_CONTENT) 


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer


# class CustomChangePasswordApiView(generics.UpdateAPIView):
class CustomChangePasswordApiView(generics.GenericAPIView):
    """
        we use generic api view instead of update api view because we dont need patch in this endpoint but
        update api view add patch endpoint beside of put method in endpoints and we can see it in swagger!!
    """
    # model=User
    permission_classes=[IsAuthenticated]
    serializer_class=ChangePasswordSerializer
    queryset=User.objects.all()

    def get_object(self):
        obj=self.request.user
        return obj
    
    # def update(self, request, *args, **kwargs): # UpdateAPIView
    def put(self, request, *args, **kwargs): # GenericAPIView
        self.object=self.get_object()
        
        # serializer=self.get_serializer(data=request.data)
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            #check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password":["wrong password."]},status=status.HTTP_400_BAD_REQUEST)
            
            # set password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            
            return Response({'details':"password changed successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserProfileApiView(generics.RetrieveUpdateAPIView):
    """for dont passig pk or lookup field to retrieve or update methods of view we can just override get object method of view"""
    serializer_class=UserProfileModelSerializer
    permission_classes=[IsAuthenticated]
    queryset=Profile.objects.all()

    def get_object(self):
        queryset=self.get_queryset()
        obj=get_object_or_404(queryset,user=self.request.user)
        return obj
    

class SendTestEmail(generics.GenericAPIView):
    serializer_class=UserProfileModelSerializer

    def get(self, request, *args, **kwargs):

        send_mail('email/test_email.tpl', {'name': 'bahmanpn'}, 'admin@gmail.com', ['bahmanpn@gmail.com'])
        # send_mail(
        #         'Subject here',
        #         'here is the message',
        #         'from@example.com',
        #         ['to@example.com'],
        #         fail_silently=True
        #         )
        print('email sent to user successfully')
        return Response('email sent')