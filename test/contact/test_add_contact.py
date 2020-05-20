from python_training.model.contact import Contact

    
def test_add_new_contact(app):
    app.contact.add_new(Contact(name="name", surname="surname", address="address", mob_phone="+380xxxxxxxxxx"))
    app.session.logout()


def test_add_empty_contact(app):
    app.contact.add_new(Contact(name="", surname="", address="", mob_phone=""))
