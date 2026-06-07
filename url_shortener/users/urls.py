from django.urls import path
from .views import *

urlpatterns = [
    path("register/", register_user),
    path("login/", login),
    path("logout/", logout_user),

    path("allusers/", get_users),
    path("users/<uuid:user_id>/", get_user),
    path("me/", me),

    path("users/<uuid:user_id>/update/", update_user),
    path("users/<uuid:user_id>/delete/", delete_user),
]