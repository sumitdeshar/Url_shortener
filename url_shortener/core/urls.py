from django.urls import path
from .views import *

urlpatterns = [
    path('create-short-url/', push_look_up_table, name="create url"),
    path('get-short-url/', pull_look_up_table, name="get url"),
    path('generate-short-url/', url_shortener_aka_Chhotkarily, name="url shortener aka Chhotkarily"),
]