# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(user_name="admin", user_password="secret")
    app.group.create(Group(name="test group", footer="logo of group", header="comment for group"))
    app.session.logout()
