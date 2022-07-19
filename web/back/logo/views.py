# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser

from django.shortcuts import get_object_or_404

from .serializers import LogoSerializer
from .models import Logo

# logo/
@api_view(['POST'])
@parser_classes([MultiPartParser])
def logo(request):
    newImage = {
        'image': request.data['image'],
        'video': request.data['video']
    }

    logoSerializer = LogoSerializer(data=newImage)
    if logoSerializer.is_valid():
        logoSerializer.save()
        print(logoSerializer.data)

        sample_data = [
            {
                "start": 1,
                "end": 3
            },
            {
                "start": 5,
                "end": 8
            }
        ]
        return Response(sample_data)
    else:
        print("not valid")
        return Response(logoSerializer.errors)

# logo/<int:pk>/
@api_view(['GET'])
def logo_id(request, pk):
    match_logo = get_object_or_404(Logo, id=pk)
    
    serializer = LogoSerializer(match_logo)
    return Response(serializer.data)