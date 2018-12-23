from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(first_name="created_first_name", middle_name="created_middle_name", last_name="created_last_name"))
    contact = Contact(first_name="edited_first_name", middle_name="edited_middle_name",
                      last_name="edited_last_name", nick_name="edited_nick_name",
                      title="edited_title",
                      company="Google inc.", first_address="USA", home_phone="+17637653812",
                      mobile_phone="+79276534211", work_phone="6543930383", fax="36373893333",
                      email="edited1@gmail.com", email2="edited2@inbox.ru",
                      email3="edited3@yahoo.com",
                      homepage="edited_homepage.com", birthday_day="12", birthday_month="July",
                      birthday_year="1975", anniversary_day="4", anniversary_month="March",
                      anniversary_year="2015", secondary_address="edited_USA, Boston",
                      secondary_home="New York", notes="edited_Comments"
                      )
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
