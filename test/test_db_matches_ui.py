from python_training.model.group import Group
from python_training.model.contact import Contact
from timeit import timeit


def test_group_list(app, db):
    # def clean(group):
    #     return Group(id=group.id, name=group.name.strip())
    #
    # print(timeit(lambda: app.group.get_group_list(), number=1))
    # print(timeit(lambda: map(clean, db.get_group_list()), number=1000))

    def clean(contact):
        return Contact(id=contact.id, name=contact.name.strip())

    print(timeit(lambda: app.contact.get_contacts_list(), number=1))
    print(timeit(lambda: map(clean, db.get_contact_list()), number=1000))
    assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
