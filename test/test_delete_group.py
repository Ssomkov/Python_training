import random

from model.group import Group


def test_delete_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(
            Group(name="created group", footer="created logo of group", header="created comment for group"))
    old_groups = app.group.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) + 1
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
