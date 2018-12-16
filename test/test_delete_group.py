from model.group import Group


def test_delete_contact(app):
    if app.group.count() == 0:
        app.group.create(
            Group(name="created group", footer="created logo of group", header="created comment for group"))
    app.group.delete()
