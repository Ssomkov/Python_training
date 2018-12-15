from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(first_name="edited_first_name", middle_name="edited_middle_name",
                             last_name="edited_last_name", nick_name="edited_nick_name", title="edited_title",
                             company="Google inc.", first_address="USA", home_phone="+17637653812",
                             mobile_phone="+79276534211", work_phone="6543930383", fax="36373893333",
                             email="edited1@gmail.com", email2="edited2@inbox.ru", email3="edited3@yahoo.com",
                             homepage="edited_homepage.com", birthday_day="12", birthday_month="July",
                             birthday_year="1975", anniversary_day="4", anniversary_month="March",
                             anniversary_year="2015", secondary_address="edited_USA, Boston",
                             secondary_home="New York", notes="edited_Comments"
                             )
                     )
