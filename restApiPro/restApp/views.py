from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from . import serializers
from . import models

# Create your views here.


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        usernames = [
            'Ahtesham',
            'Mazher',
            'Khan'
        ]
        return Response({'message': 'Hello', 'username': usernames})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'del'})


class HelloViewSets(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Lorum Ipsom',
            'lorie keyword',
            'khan'

        ]
        return Response({'message': 'Hello you r seeing ViewSet', 'a_viewser': a_viewset})

    def create(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
