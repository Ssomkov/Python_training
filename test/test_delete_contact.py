from random import randrange

from model.contact import Contact


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(first_name="created_first_name", middle_name="created_middle_name", last_name="created_last_name"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts) + 1
    old_contacts[index:index + 1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
