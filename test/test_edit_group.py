from model.group import Group


def test_edit_group(app):
    app.group.edit(
        Group(name="edited_test group", footer="edited_logo of group", header="edited_comment for group")
    )
