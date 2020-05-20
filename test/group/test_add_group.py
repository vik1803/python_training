# -*- coding: utf-8 -*-
from python_training.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Test Group1", header="Header", footer="Footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

