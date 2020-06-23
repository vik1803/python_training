from python_training.model.contact import Contact
from random import randrange


def test_edit_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact_id = old_contacts[index].id
    contact = Contact(name='Edited name123')
    app.contact.edit_contact_by_id(contact, contact_id)
    new_contacts = db.get_contact_list()
    old_contacts[index].name = contact.name
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contacts_list(), key=Contact.id_or_max)


def test_edit_contact_surname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact_id = old_contacts[index].id
    contact = Contact(surname='Edited Surname')
    app.contact.edit_contact_by_id(contact, contact_id)
    new_contacts = db.get_contact_list()
    old_contacts[index].surname = contact.surname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contacts_list(), key=Contact.id_or_max)


def test_edit_contact_mob_phone(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact_id = old_contacts[index].id
    contact = Contact(mob_phone='+16469804817')
    app.contact.edit_contact_by_id(contact, contact_id)
    new_contacts = db.get_contact_list()
    old_contacts[index].mob_phone = contact.mob_phone
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contacts_list(), key=Contact.id_or_max)


def test_edit_first_contact_address(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact_id = old_contacts[index].id
    contact = Contact(address='NY')
    app.contact.edit_contact_by_id(contact, contact_id)
    new_contacts = db.get_contact_list()
    old_contacts[index].address = contact.address
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contacts_list(), key=Contact.id_or_max)
