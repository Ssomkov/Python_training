from model.group import Group


def test_edit_group(app):
    app.session.login(user_name="admin", user_password="secret")
    app.group.edit(
        Group(name="edited_test group", footer="edited_logo of group", header="edited_comment for group")
    )
    app.session.logout()
