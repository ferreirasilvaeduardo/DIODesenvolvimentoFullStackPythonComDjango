from http import HTTPStatus

import pytest
from django.contrib.auth.models import Permission, User
from django.urls import reverse


def test_contacts_thanks(client):
    # Give
    name = "Jhon"
    # When
    url = reverse("contacts:thanks", kwargs={"name": name})
    response = client.get(url)
    # Then
    resultado = f"Obrigado! {str(name).strip().capitalize()}"
    assert response.content.decode("utf-8") == resultado
    assert response.status_code == HTTPStatus.OK


# def test_contacts_create_unauthenticated_user(client):
# Give
# When
# Then


def test_contacts_create_unauthenticated_user(client):
    # Give
    url_expected = f"{reverse('accounts:login')}?next={reverse('contacts:create')}"
    # When
    url = reverse("contacts:create")
    response = client.get(url)
    # Then
    assert response.status_code == HTTPStatus.FOUND  # FORBIDDEN
    assert url_expected == response.url


# @pytest.mark.skip
@pytest.mark.django_db
def test_contacts_create_sucess(client):
    # Give
    data = {
        "name": "Assunto",
        "message": "Mensagem",
        "sender": "sender@sender.com.br",
        "cc_myself": True,
    }
    url_expected = f"{reverse('accounts:login')}?next={reverse('contacts:create')}"
    user = User.objects.create(
        username="Jonh", email="teste@teste.com", password="123Jonh"
    )
    # When
    url = reverse("contacts:create")
    response = client.post(url, data)
    # Then
    # breakpoint()
    client.force_login(user)
    permission = Permission.objects.get(codename="add_contact")
    user.user_permissions.add(permission)
    assert response.status_code == HTTPStatus.FOUND  # FORBIDDEN
    assert url_expected == response.url
