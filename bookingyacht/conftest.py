import pytest
from django.contrib.auth.models import User

from bookingyacht.models import Yacht, CharterCompany, Marina


@pytest.fixture
def user():
    u = User()
    u.username = 'kazik'
    u.set_password("Qwerty161!")
    u.save()
    return u


@pytest.fixture
def marina():
    c = Marina()
    c.name = "sukosan"
    c.city = "przyklad"
    c.country = "Chorwacja"
    c.save()
    return c


@pytest.fixture
def charter_company(marina):
    c = CharterCompany()
    c.name = "sukosan"
    c.save()
    c.marina.add(marina)
    return c


@pytest.fixture
def yacht(user, charter_company):
    ts = []
    t = Yacht()

    t.name = 'jakis jacht'
    t.year = 1992
    t.length = 25
    t.max_person = 10
    t.price = 2222
    t.category = 1
    t.charter_company = charter_company

    t.save()
    ts.append(t)

    return ts
