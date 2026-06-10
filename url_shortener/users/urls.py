from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout"),

    # path("allusers/", get_users),
    # path("users/<uuid:user_id>/", get_user),
    # path("me/", me),

    # path("users/<uuid:user_id>/update/", update_user),
    # path("users/<uuid:user_id>/delete/", delete_user),
]
print(urlpatterns)