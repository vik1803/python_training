from python_training.model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", surname="", address="", mob_phone="", home_phone="", work_phone="", secondary_phone="",
                    email_1="", email_2="", email_3="")] + [
    Contact(name=random_string("name", 10), surname=random_string("surname", 20), address=random_string("address", 30),
            mob_phone=random_string("mob_phone", 13), home_phone=random_string("home_phone", 13),
            work_phone=random_string("work_phone", 13), secondary_phone=random_string("secondary_phone", 13),
            email_1=random_string("mail1", 15), email_2=random_string("mail2", 15), email_3=random_string("mail3", 15)
            ) for i in range(5)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

