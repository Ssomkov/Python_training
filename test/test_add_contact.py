# -*- coding: utf-8 -*-
import random
import string

import pytest

from model.contact import Contact


def get_random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


def get_random_email(prefix, max_length):
    symbols = string.ascii_letters + string.digits
    return prefix + "@" + "".join(
        [random.choice(symbols) for i in range(random.randrange(max_length))]) + "." + "".join(
        [random.choice(string.ascii_letters) for i in range(random.randrange(max_length))])


def get_random_homepage(prefix, max_length):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join(
        [random.choice(symbols) for i in range(random.randrange(max_length))]) + "." + "".join(
        [random.choice(string.ascii_letters) for i in range(random.randrange(max_length))])


def get_random_digit(start_value, max_value):
    return "".join(str(random.randrange(start_value, max_value)))


def get_random_phone(max_length):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


def get_random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return random.choice(months)


test_data = [Contact(first_name=get_random_string("fname", 5), middle_name=get_random_string("mname", 5),
                     last_name=get_random_string("lname", 5),
                     nick_name=get_random_string("Lebovsky", 5), title=get_random_string("Contact title", 5),
                     company=get_random_string("Google inc.", 5),
                     first_address=get_random_string("USA", 5), home_phone=get_random_phone(15),
                     mobile_phone=get_random_phone(15),
                     work_phone=get_random_phone(15), fax=get_random_phone(15),
                     email=get_random_email("email1", 5),
                     email2=get_random_email("email2", 5), email3=get_random_email("email3", 5),
                     homepage=get_random_homepage("page", 5),
                     birthday_day=get_random_digit(1, 30), birthday_month=get_random_month(),
                     birthday_year=get_random_digit(1960, 1990),
                     anniversary_day=get_random_digit(1, 25), anniversary_month=get_random_month(),
                     anniversary_year=get_random_digit(2000, 2017),
                     group="[none]", secondary_address=get_random_string("USA", 10),
                     secondary_phone=get_random_phone(15),
                     notes=get_random_string("Comments", 20)
                     ) for i in range(2)
             ]


def get_ids():
    return [repr(x) for x in test_data]


@pytest.mark.parametrize("contact", test_data, ids=get_ids())
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
