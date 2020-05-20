from python_training.model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    app.contact.delete_first_contact()
