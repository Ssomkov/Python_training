import random

from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(first_name="created_first_na", middle_name="created_middle_na", last_name="created_last_na"))
    contact = Contact(first_name="edited_first_na", middle_name="edited_middle_na",
                      last_name="edited_last_nam", nick_name="edited_nick_name",
                      title="edited_title",
                      company="Google inc.", first_address="USA", home_phone="+17637653812",
                      mobile_phone="+79276534211", work_phone="6543930383", fax="36373893333",
                      email="edited1@gmail.com", email2="edited2@inbox.ru",
                      email3="edited3@yahoo.com",
                      homepage="edited_homepage.com", birthday_day="12", birthday_month="July",
                      birthday_year="1975", anniversary_day="4", anniversary_month="March",
                      anniversary_year="2015", secondary_address="edited_USA, Boston",
                      secondary_phone="4234234234", notes="edited_Comments"
                      )
    old_contacts = db.get_contact_list()
    contact_for_edit = random.choice(old_contacts)
    id = contact_for_edit.id
    contact.id = id
    app.contact.edit_by_id(contact_for_edit.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for i in range(len(old_contacts)):
        if old_contacts[i].id == contact_for_edit.id:
            old_contacts[i] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(),
                                                                     key=Contact.id_or_max)
