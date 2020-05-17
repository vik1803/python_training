# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(name="name", surname="surname", addr="address", mob_phone="+380xxxxxxxxxx"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(name="", surname="", addr="", mob_phone=""))
    app.logout()
