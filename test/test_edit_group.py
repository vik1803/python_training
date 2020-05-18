from python_training.model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Edited Group1 upd", header="Header upd", footer="Footer upd"))
    app.session.logout()