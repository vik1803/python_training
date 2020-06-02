from python_training.model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    str1 = string.ascii_letters + string.digits + string.punctuation + " "*10
    str2 = str1.replace("'", "")
    symbols = str2.replace('"', "")
    return prefix + "".join([random.choice(symbols.strip()) for i in range(random.randrange(maxlen))])


testdata = [Contact(name='', surname='', address='', mob_phone='', home_phone='', secondary_phone='', work_phone='',
                    email_1='', email_2='', email_3='')] + \
           [Contact(name=random_string('name', 10), surname=random_string('surname', 10),
                    address=random_string('address', 20), mob_phone=random_string('mob_phone', 12),
                    home_phone=random_string('home_phone', 12), secondary_phone=random_string('secondary_phone', 12),
                    work_phone=random_string('work_phone', 12), email_1=random_string('email', 13),
                    email_2=random_string('email_2', 13), email_3=random_string('email_3', 13)) for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))
