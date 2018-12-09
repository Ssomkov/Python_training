def test_delete_contact(app):
    app.session.login(user_name="admin", user_password="secret")
    app.contact.delete()
    app.session.logout()
