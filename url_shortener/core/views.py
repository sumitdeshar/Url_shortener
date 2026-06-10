from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.cache import cache

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .utlis import generate_shortcode, build_char_map, build_short_url, increment_click, increment_click_from_cache
from .models import CharMap, Link
import threading

from .serializers import *

User = get_user_model()

# Create your views here.

@api_view(['POST'])
def create_lookup_table(request):
    try:
        lookup_entry = CharMap.objects.first()
        if lookup_entry:
            char_map = lookup_entry.char_map # type: ignore
        
        if not lookup_entry:
            char_map=build_char_map()
            print(char_map)
                
            if not char_map:
                return JsonResponse(
                    {"error": "Lookup table generation failed"},
                    status=400
                )
            CharMap.objects.create(char_map=char_map)
            print('done create hash matrix')
                    
            return JsonResponse(
                {
                    "message": "Lookup already created successfully",
                    "char_map": char_map
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
        original_url = serializer.validated_data["original_url"] # type: ignore
        shortcode_length = serializer.validated_data["shortcode_length"] # type: ignore
        custom_domain = serializer.validated_data['domain'] # type: ignore
        
        lookup_entry=CharMap.objects.first()
        # char_map = CharMapSerializer(lookup_entry).data  #dont do this you would have to handle for so many case going wrong so, pass direct column of data
        
        if not lookup_entry:
            return JsonResponse({"error": "Lookup table missing"}, status=400)
        char_map = lookup_entry.char_map

        shortcode = generate_shortcode(shortcode_length, char_map) # type: ignore
        print(shortcode)
        # print ('done serializing4')
        
        if shortcode:
            short_url=build_short_url(shortcode=shortcode, user_domain=custom_domain)
            
            link_obj = Link.objects.create(
            short_link=shortcode,
            original_link=original_url,
            owner=request.user,
            domain=custom_domain
        )
            # print ('done serializing5')

            return Response({
            "link": LinkResponseSerializer(link_obj).data,
            "short_url": short_url
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


#have not been full tested work for basic conditions 
def redirect_short_url(request, shortcode):
    cached_url = cache.get(shortcode)

    if cached_url:
        threading.Thread(
            target=increment_click_from_cache,
            args=(shortcode,)
        ).start()

        return redirect(cached_url)

    link = get_object_or_404(Link, short_link=shortcode, is_active=True)
    cache.set(shortcode, link.original_link, timeout=60 * 60 * 24 * 30)

    threading.Thread(
        target=increment_click, 
        args=(link.id,)
        ).start()

    return redirect(link.original_link)