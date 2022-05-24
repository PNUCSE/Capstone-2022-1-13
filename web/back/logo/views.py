# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser

from django.shortcuts import get_object_or_404

from .serializers import LogoSerializer
from .models import Logo

# logo/
@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser])
def logo(request):
    if request.method == "GET" :
        user = request.user
      
        match_logos = Logo.objects.filter(uploader=user)

        if not match_logos:
            return Response({"message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LogoSerializer(match_logos, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        user = request.user
        newImage = {
            'image': request.data['image'],
            'uploader': user.id
        }

        logoSerializer = LogoSerializer(data=newImage)
        if logoSerializer.is_valid():
            logoSerializer.save()
        else:
            return Response(logoSerializer.errors)

        return Response(logoSerializer.data)

# logo/<int:pk>/
@api_view(['GET'])
def logo_id(request, pk):
    user = request.user
    match_logo = get_object_or_404(Logo, id=pk)

    if match_logo.uploader != user :
        return Response(status.HTTP_406_NOT_ACCEPTABLE)
    
    serializer = LogoSerializer(match_logo)
    return Response(serializer.data)