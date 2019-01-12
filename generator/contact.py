import getopt
import os.path
import random
import string
import sys

import jsonpickle

from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                     ) for i in range(n)
             ]


def get_ids():
    return [repr(x) for x in test_data]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
