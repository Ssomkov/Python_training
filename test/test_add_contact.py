# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(user_name="admin", user_password="secret")
    app.add_contact(Contact(first_name="Chuvak", middle_name="Chuvakovich", last_name="Lebovsky",
                            nick_name="Lebovsky", title="Contact title", company="Google inc.",
                            first_address="USA", home_phone="+17637653812", mobile_phone="+79276534211",
                            work_phone="6543930383", fax="36373893333", email="lebovsky@gmail.com",
                            email2="lebovsky@inbox.ru", email3="lebovsky@yahoo.com", homepage="google.com",
                            birthday_day="12", birthday_month="July", birthday_year="1975",
                            anniversary_day="4", anniversary_month="March", anniversary_year="2015",
                            group="[none]", secondary_address="USA, Boston", secondary_home="New York",
                            notes="Comments"
                            )
                    )
    app.session.logout()
