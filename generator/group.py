import getopt
import json
import os.path
import random
import string
import sys

from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def get_random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


test_data = [Group(name=get_random_string("group name", 10), footer=get_random_string("group footer", 10),
                   header=get_random_string("group header", 10)) for i in range(n)
             ]


def get_ids():
    return [repr(x) for x in test_data]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
