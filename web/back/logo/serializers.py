from rest_framework import serializers
from .models import Logo

class LogoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    video = serializers.FileField(use_url=True)

    class Meta:
        model = Logo
        fields = ('image', 'video')