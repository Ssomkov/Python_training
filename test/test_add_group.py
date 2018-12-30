# -*- coding: utf-8 -*-

import random
import string

import pytest

from model.group import Group


def get_random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


test_data = [Group(name=get_random_string("group name", 10), footer=get_random_string("group footer", 10),
                   header=get_random_string("group header", 10)),
             Group(name=get_random_string("group name", 10), footer=get_random_string("group footer", 10),
                   header=get_random_string("group header", 10))]


def get_ids():
    return [repr(x) for x in test_data]


@pytest.mark.parametrize("group", test_data, ids=get_ids())
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
