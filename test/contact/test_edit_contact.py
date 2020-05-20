from python_training.model.contact import Contact


def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    app.contact.edit_first_contact(Contact(name='edited name'))


def test_edit_contact_surname(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    app.contact.edit_first_contact(Contact(surname='Edited Surname'))


def test_edit_contact_mob_phone(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    app.contact.edit_first_contact(Contact(mob_phone='+16469804817'))


def test_edit_contact_address(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    app.contact.edit_first_contact(Contact(address='NY'))
