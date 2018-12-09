def test_delete_contact(app):
    app.session.login(user_name="admin", user_password="secret")
    app.group.delete_group()
    app.session.logout()
