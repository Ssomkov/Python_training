# -*- coding: utf-8 -*-
import allure

from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with allure.step('Get contact list from DB'):
        old_contacts = db.get_contact_list()
    with allure.step('Create contact %s' % contact):
        app.contact.create(contact)
    with allure.step('Verify contact was added'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
