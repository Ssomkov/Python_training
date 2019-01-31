import re

from model.contact import Contact


def test_contacts_info_on_home_page(app, db):
    contacts_from_bd = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

    for item in range(len(contacts_from_bd)):
        assert contacts_from_bd[item].first_name == contacts_from_page[item].first_name
        assert contacts_from_bd[item].last_name == contacts_from_page[item].last_name
        assert contacts_from_bd[item].first_address == contacts_from_page[item].first_address
        assert contacts_from_page[item].all_phones_from_home_page == merge_phones_like_on_home_page(
            contacts_from_bd[item])
        assert contacts_from_page[item].all_emails_from_home_page == merge_emails_like_on_home_page(
            contacts_from_bd[item])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                                           contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email2, contact.email3])))
