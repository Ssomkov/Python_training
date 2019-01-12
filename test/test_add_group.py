# -*- coding: utf-8 -*-
import pytest

from data.add_group import test_data, get_ids
from model.group import Group


@pytest.mark.parametrize("group", test_data, ids=get_ids())
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
