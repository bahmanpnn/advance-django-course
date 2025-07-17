from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer


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
    