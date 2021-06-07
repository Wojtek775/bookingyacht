import pytest as pytest
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from bookingyacht.conftest import yacht
from bookingyacht.models import Yacht


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'johnpassword')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_client():
    Client()


@pytest.mark.django_db
def test_add_yacht_get_not_logged_in():
    c = Client()
    url = reverse('add_yacht')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_add_yacht_get_logged_in(user):
    c = Client()
    c.force_login(user)
    url = reverse('add_yacht')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_yacht(user, yacht):
    c = Client()
    c.force_login(user)
    url = reverse('add_yacht')
    response = c.post(url,
                      {'name': 'alamakota', 'year': 1992, 'length': 25, 'max_person': 10, 'price': 255, 'category': 1,
                       'charter_company': 1})
    assert response.status_code == 302
    assert Yacht.objects.count() == 2


@pytest.mark.django_db
def test_view_yacht(client):
    url = reverse('view_yacht')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_yacht_view_get(yacht):
    c = Client()
    url = reverse('view_yacht')
    response = c.get(url)
    yachts = response.context['yacht']
    assert response.status_code == 200
    assert yachts.count() == len(yachts)


@pytest.mark.django_db
def test_reserve_yacht(user, yacht):
    c = Client()
    c.force_login(user)
    url = reverse('reserve-yacht', args=(yacht[0].id,))
    response = c.post(url,
                      {'reservation-date': '2021-08-09'})
    assert response.status_code == 302

