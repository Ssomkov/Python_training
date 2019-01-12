import random
import string

from model.group import Group


def get_random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


test_data = [Group(name=get_random_string("group name", 10), footer=get_random_string("group footer", 10),
                   header=get_random_string("group header", 10)) for i in range(3)
             ]


def get_ids():
    return [repr(x) for x in test_data]
