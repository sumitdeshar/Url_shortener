from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework import status
from .utlis import createshortcode, generate_url

from .serializers import *

User = get_user_model()

# Create your views here.
@api_view(["POST"])
def url_shortener_aka_Chhotkarily(request):
    try:
        print('got data')
        jsondata = request.data
        serializer = UrlSerializer(data=jsondata)
        print ('done serializing')
        if serializer.is_valid():
            original_url = serializer.validated_data.get("original_url")
            
        shortcode = createshortcode(serializer.shortcode_length)
            
        # short_url = generate_url()
        
        
        
        return JsonResponse({
            'original': original_url,
            'short url': shortcode,
        })
        

            
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )
    