from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .utlis import generate_shortcode, build_char_map, build_short_url
from .models import CharMap, Link

from .serializers import *

User = get_user_model()

# Create your views here.
@api_view(['POST'])
def create_lookup_table(request):
    try:
        lookup_entry = CharMap.objects.first()
        char_map = lookup_entry.hash_matrix
        
        if not char_map:
            char_map=build_char_map()
            print(char_map)
                
            if not char_map:
                return JsonResponse(
                    {"error": "Lookup table generation failed"},
                    status=400
                )
            CharMap.objects.create(hash_matrix=char_map)
            print('done create hash matrix')
                    
            return JsonResponse(
                {
                    "message": "Lookup table created successfully"
                },
                status=201
            )
        else:
            return JsonResponse(
                {
                    "message": "Lookup already created successfully",
                    "char_map": char_map
                },
                status=200
            )
            
            
    except Exception as e:
         return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )
         
         
         
@api_view(['GET'])
def get_lookup_table(request):
    try:
        serializer = CharMapSerializer(
            CharMap.objects.all(),
                many=True
                )

        return Response(
            serializer.data,
            status=200
            )
    
    except Exception as e:
         return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def shorten_url(request):
    try:
        payload = request.data
        serializer = UrlSerializer(data=payload)

        
        serializer.is_valid(raise_exception=True)
        original_url = serializer.validated_data["original_url"]
        shortcode_length = serializer.validated_data["shortcode_length"]
        
        lookup_entry=CharMap.objects.first()
        # char_map = CharMapSerializer(lookup_entry).data
        #pass proper data
        if not lookup_entry:
            return JsonResponse({"error": "Lookup table missing"}, status=400)
        char_map = lookup_entry.hash_matrix

        shortcode_result = generate_shortcode(shortcode_length=shortcode_length,char_map=char_map)
        print(shortcode_result)
        print ('done serializing4')
        
        if shortcode_result:
            short_url=build_short_url(shortcode=shortcode_result['shortcode'])
            
            Link.objects.create(short_link=short_url, original_link=original_url, owner=request.user)
            print ('done serializing5')

            return JsonResponse({
                'original': original_url,
                'short url': short_url,
            })
        else:
            return JsonResponse({
                "error": "Shortcode is not generated"
            }
            )
        
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )
    