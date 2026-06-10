from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UrlSerializer(serializers.Serializer):
    original_url = serializers.URLField()
    shortcode_length = serializers.IntegerField()
    domain = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
class CharMapSerializer(serializers.Serializer):
    # name = serializers.CharField()
    char_map = serializers.JSONField()
