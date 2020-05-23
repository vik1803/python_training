from python_training.model.contact import Contact


def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(name='edited name')
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0].name = contact.name
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_surname(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(surname='Edited Surname')
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0].surname = contact.surname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_mob_phone(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(mob_phone='+16469804817')
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_address(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(address='NY')
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

