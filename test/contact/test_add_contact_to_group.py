from python_training.fixture.orm import ORMFixture
from python_training.model.contact import Contact
from python_training.model.group import Group


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_new_contact_to_group(app):
    if len(db.get_group_list_orm()) == 0:
        app.group.create(Group(name='test'))
    # Select group to adding contacts
    groups_list = sorted(db.get_group_list_orm(), key=Group.id_or_max)
    group_id = groups_list[-1].id
    # Add at least one contact to group to avoid errors
    app.contact.add_new(Contact(name=''), group_id)
    # Get number of group members
    old_members = len(db.get_contacts_in_group_orm(Group(id='%s' % group_id)))
    # Add one more group member
    app.contact.add_new(Contact(name=''), group_id)
    contacts_list = sorted(db.get_contact_list_orm(), key=Contact.id_or_max)
    contact_id = contacts_list[-1].id
    # Check that one more member was added to group
    new_members = sorted(db.get_contacts_in_group_orm(Group(id='%s' % group_id)), key=Contact.id_or_max)
    assert len(new_members) == old_members + 1
    assert new_members[-1].id == contact_id

