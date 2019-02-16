import random

from pytest_bdd import when, then, given

from model.group import Group


@given('a group list')
def group_list(db):
    return db.get_group_list()


@given('group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer);


@when('I add the group to list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="empty_name", header="empty_header", footer="empty_footer"))
    return db.get_group_list()


@given('a random group from list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete a group from list')
def delete_group(app, random_group):
    app.group.delete_by_id(random_group.id)


@then('the new group list is equal to the old list without deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) + 1
    old_groups.remove(random_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
