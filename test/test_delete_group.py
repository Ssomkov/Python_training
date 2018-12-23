from random import randrange

from model.group import Group


def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(
            Group(name="created group", footer="created logo of group", header="created comment for group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) + 1
    old_groups[index:index + 1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
