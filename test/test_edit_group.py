from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(
            Group(name="created group", footer="created logo of group", header="created comment for group"))
    app.group.edit(
        Group(name="edited_test group", footer="edited_logo of group", header="edited_comment for group")
    )
