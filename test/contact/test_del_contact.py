from python_training.model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

