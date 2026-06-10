from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name="home"),
    path('create-short-url/', create_lookup_table, name="create url"),
    path('get-short-url/', get_lookup_table, name="get url"),
    path('generate-short-url/', shorten_url, name="url shortener aka Chhotkarily"),
]