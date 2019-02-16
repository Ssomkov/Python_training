# -*- coding: utf-8 -*-
import pytest

from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Get group list from DB'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Create group %s' % group):
        app.group.create(group)
    with pytest.allure.step('Verify group was added'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
