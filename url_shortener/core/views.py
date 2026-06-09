from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .utlis import createshortcode, generate_lookup, generate_url
from .models import LookUpTable, ShortCode, LinkTable

from .serializers import *

User = get_user_model()

# Create your views here.
@api_view(['POST'])
def push_look_up_table(request):
    try:
        lookup_table = LookUpTable.objects.all()
        
        if not lookup_table:
            lookup_table=generate_lookup()
            print(lookup_table)
                
            if not lookup_table:
                return JsonResponse(
                    {"error": "Lookup table generation failed"},
                    status=400
                )
            LookUpTable.objects.create(hash_matrix=lookup_table)
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
                    "message": "Lookup already created successfully"
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
def pull_look_up_table(request):
    try:
        serializer = LookUpTableSerializer(
            LookUpTable.objects.all(),
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
def url_shortener_aka_Chhotkarily(request):
    try:
        jsondata = request.data
        serializer = UrlSerializer(data=jsondata)

        
        serializer.is_valid(raise_exception=True)
        original_url = serializer.validated_data["original_url"]
        shortcode_length = serializer.validated_data["shortcode_length"]
        
        lookup_model=LookUpTable.objects.first()
        # lookup_table = LookUpTableSerializer(lookup_model).data
        #pass proper data
        if not lookup_model:
            return JsonResponse({"error": "Lookup table missing"}, status=400)
        lookup_table = lookup_model.hash_matrix

        shortcode = createshortcode(shortcode_length=shortcode_length,lookup_table=lookup_table)
        print ('done serializing4')
        
        if shortcode:
            short_url=generate_url(shortcode=shortcode)
            
            LinkTable.objects.create(short_link=short_url, original_link=original_url, owner=request.user)
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
    