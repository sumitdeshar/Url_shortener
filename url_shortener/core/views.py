from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework import status

from .serailizers import *

User = get_user_model()

# Create your views here.
@api_view(["POST"])
def url_shortener_aka_Chhotkarily(request):
    try:
        jsondata = request.data
        serializer = UrlSerializer(data=jsondata)
        
        if serializer.is_valid():
            original_url = serializer.validated_data.get("original_url")
            
        print(original_url)
        

            
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )
    