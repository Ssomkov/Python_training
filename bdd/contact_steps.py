from pytest_bdd import when, then, given

from model.contact import Contact


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
