from python_training.model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(name="Test", surname="Updated", addr="NY", mob_phone="+16469804817"))
    app.session.logout()
