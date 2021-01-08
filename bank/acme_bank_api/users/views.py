from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from acme_bank_api.users.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

# Create your views here.

class UserCreate(APIView):
#class UserCreate(generics.CreateAPIView):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
