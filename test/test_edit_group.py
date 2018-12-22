from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(
            Group(name="created group", footer="created logo of group", header="created comment for group"))
    group = Group(name="edited_test group", footer="edited_logo of group", header="edited_comment for group")
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
