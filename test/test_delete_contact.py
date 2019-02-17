import random

import allure

from model.contact import Contact


def test_delete_random_contact(app, db, check_ui):
    with allure.step('Create contact if not exists'):
        if app.contact.count() == 0:
            app.contact.create(
                Contact(first_name="created_first_name", middle_name="created_middle_name",
                        last_name="created_last_name"))
    old_contacts = db.get_contact_list()
    with allure.step('Get random contact'):
        contact = random.choice(old_contacts)
    with allure.step('Delete contact %s' % contact):
        app.contact.delete_by_id(contact.id)
    with allure.step('Verify contact was deleted'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts) + 1
        old_contacts.remove(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
