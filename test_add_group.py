# -*- coding: utf-8 -*-
import pytest

from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user_name="admin", user_password="secret")
    app.create_group(Group(name="test group", footer="logo of group", header="comment for group"))
    app.logout()
