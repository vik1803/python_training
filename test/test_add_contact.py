# -*- coding: utf-8 -*-
import pytest
from python_training.fixture.application import Application
from python_training.model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(name="name", surname="surname", addr="address", mob_phone="+380xxxxxxxxxx"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(name="", surname="", addr="", mob_phone=""))
    app.session.logout()
