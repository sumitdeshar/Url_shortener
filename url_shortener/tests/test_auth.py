import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_register_user():

    client = APIClient()

    payload = {
        "username": "useristesting",
        "email": "test@testample.com",
        "password": "pass1234567",
        "password2": "pass1234567"
    }

    response = client.post("/users/register/", payload)

    assert response.status_code == 200
    assert User.objects.filter(username="useristesting").exists()
    
@pytest.mark.django_db
def test_login_user():

    client = APIClient()

    User.objects.create_user(
        username="useristesting",
        email="test@testample.com",
        password="pass1234567"
    )

    payload = {
        "username": "useristesting",
        "password": "pass1234567"
    }

    response = client.post("/users/login/", payload)

    assert response.status_code == 200
    assert "user_id" in response.json()