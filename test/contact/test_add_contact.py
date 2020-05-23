from python_training.model.contact import Contact

    
def test_add_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = (Contact(name="name", surname="surname", address="address", mob_phone="+380xxxxxxxxxx"))
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(name="", surname="", address="", mob_phone="")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
