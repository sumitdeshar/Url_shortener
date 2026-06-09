from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate
from django.contrib import auth

from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *

User = get_user_model()

# Create your views here.
@api_view(["POST"])
def  register_user(request):
    try:
        payload = request.data
        serializer = UserRegistrationSerializer(data=payload)
        
        if serializer.is_valid():
            
            username = serializer.validated_data.get("username")
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            password2 = serializer.validated_data.get("password2")
        
            if password == password2:
                if User.objects.filter(email=email).exists():
                    return JsonResponse({'error': 'Email Already Used'}, status=status.HTTP_400_BAD_REQUEST)
                elif User.objects.filter(username=username).exists():
                    return JsonResponse({'error': 'Username Already Used'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    # user.save() redundant
                    return JsonResponse({'message': 'Registration successful'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': 'Password did not match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'error_messages': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )


@api_view(["POST"])
def login(request):
    try:
        payload = request.data
        serializer = LoginSerializer(data=payload)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:
                auth.login(request, user)

            return JsonResponse(
                {
                    "message": "Login successful",
                    "user_id": str(user.id)
                },
                status=status.HTTP_200_OK
            )

        return JsonResponse(
            {
                "error": "Invalid username or password"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )
        
@api_view(["POST"])
def logout_user(request):

    auth.logout(request)

    return JsonResponse(
        {
            "message": "Logout successful"
        },
        status=200
    )
        
@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    print(users)
    
    if not users.exists():
        return JsonResponse(
                    {
            "message": "None of the user were found"
        },
        status=304
        )
    else:

        serializer = UserBaseSerializer(users, many=True)

    return JsonResponse(
        serializer.data,
        safe=False,
        status=200
    )
    
@api_view(["GET"])
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        serializer = UserBaseSerializer(user)

        return JsonResponse(serializer.data)

    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"},
            status=404
        )
@api_view(["GET"])
def me(request):

    if not request.user.is_authenticated:
        return JsonResponse(
            {"error": "Not authenticated"},
            status=401
        )

    serializer = UserBaseSerializer(request.user)

    return JsonResponse(serializer.data)

@api_view(["PUT"])
def update_user(request, user_id):

    try:
        user = User.objects.get(id=user_id)

        user.first_name = request.data.get(
            "first_name",
            user.first_name
        )

        user.last_name = request.data.get(
            "last_name",
            user.last_name
        )

        user.bio = request.data.get(
            "bio",
            user.bio
        )

        user.save()

        serializer = UserBaseSerializer(user)

        return JsonResponse(serializer.data)

    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"},
            status=404
        )
        
@api_view(["DELETE"])
def delete_user(request, user_id):

    try:
        user = User.objects.get(id=user_id)

        user.delete()

        return JsonResponse(
            {"message": "User deleted"}
        )

    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"},
            status=404
        )
        
        
        
        
        
##order_by       
# users = User.objects.order_by("username")
# Descending:
# users = User.objects.order_by("-username")
# Newest first:
# users = User.objects.order_by("-created_at")

##filtering
# Get users whose username contains "sum":
# users = User.objects.filter(
#     username__icontains="sum"
# )

# Email search:
# users = User.objects.filter(
#     email__icontains="gmail"
# )

## group_by:
# from django.db.models import Count
# users = (
#     User.objects
#     .values("is_staff")
#     .annotate(total=Count("id"))
# )

