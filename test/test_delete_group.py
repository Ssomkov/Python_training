from model.group import Group


def test_delete_contact(app):
    if app.group.count() == 0:
        app.group.create(
            Group(name="created group", footer="created logo of group", header="created comment for group"))
    old_groups = app.group.get_group_list()
    app.group.delete()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) + 1
