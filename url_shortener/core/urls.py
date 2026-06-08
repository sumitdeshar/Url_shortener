from django.urls import path
from .views import *

urlpatterns = [
    path('/generate-short-url', url_shortener_aka_Chhotkarily, name="url_shortener_aka_Chhotkarily"),
]