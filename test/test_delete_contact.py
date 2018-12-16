from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(first_name="created_first_name", middle_name="created_middle_name", last_name="created_last_name"))
    app.contact.delete()
