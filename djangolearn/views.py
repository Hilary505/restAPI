from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from djangolearn.models import Location
from djangolearn.serializers import LocationSerializers

@api_view(['GET','POST'])


# Create your views here.

def my_location(request):
    if request.method == "GET":
        snippets = Location.objects.all()
        serializers = LocationSerializers(snippets,many=True)
        return Response(serializers.data)

    elif request.method == "POST":
        serializers = LocationSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

