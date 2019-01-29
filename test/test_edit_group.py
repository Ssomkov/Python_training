import random

from model.group import Group


def test_edit_random_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(
            Group(name="created group", footer="created logo of group", header="created comment for group"))
    group = Group(name="edited_test group", footer="edited_logo of group", header="edited_comment for group")
    old_groups = db.get_group_list()
    group_for_edit = random.choice(old_groups)
    id = group_for_edit.id
    group.id = id
    app.group.edit_by_id(group_for_edit.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    for i in range(len(old_groups)):
        if old_groups[i].id == group_for_edit.id:
            old_groups[i] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
