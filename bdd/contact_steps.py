from pytest_bdd import when, then, given

from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('contact with <first_name>, <middle_name> and <last_name>')
def new_contact(first_name, middle_name, last_name):
    return Contact(first_name=first_name, middle_name=middle_name, last_name=last_name)


@when('I add the contact to list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="empty_name", middle_name="empty_name", last_name="empty_name"))
    return db.get_contact_list()


@given('a random contact from list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete a contact from list')
def delete_contact(app, random_contact):
    app.contact.delete_by_id(random_contact.id)


@then('the new contact list is equal to the old list without deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts) + 1
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


@when('I edit a random contact from list')
def edit_random_contact(app, random_contact):
    id = random_contact.id
    new_contact.id = id
    app.contact.edit_by_id(random_contact.id, new_contact)


@then('the new contact list is equal to the old contact list with the edited contact')
def verify_contact_edited(db, non_empty_contact_list, random_contact, app, check_ui, new_contact):
    new_contacts = db.get_contact_list()
    old_contacts = non_empty_contact_list
    contact_for_edit = random_contact
    contact = new_contact
    assert len(old_contacts) == len(new_contacts)
    for i in range(len(old_contacts)):
        if old_contacts[i].id == contact_for_edit.id:
            old_contacts[i] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
