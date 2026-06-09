from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# class UserURLSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "id",
#             "username",
#             "email",
#         ]

class UrlSerializer(serializers.Serializer):
    original_url = serializers.URLField()
    shortcode_length = serializers.IntegerField()
    
class LookUpTableSerializer(serializers.Serializer):
    # name = serializers.CharField()
    hash_matrix = serializers.JSONField()
