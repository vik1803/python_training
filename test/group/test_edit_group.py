from python_training.model.group import Group
from random import randrange


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group_id = old_groups[index].id
    group = Group(name="Edited name")
    app.group.edit_group_by_id(group, group_id)
    new_groups = db.get_group_list()
    old_groups[index].name = group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_edit_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group_id = old_groups[index].id
    group = Group(header="Edited header")
    app.group.edit_group_by_id(group, group_id)
    new_groups = db.get_group_list()
    old_groups[index].header = group.header
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_edit_first_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group_id = old_groups[index].id
    group = Group(footer="Edited footer")
    app.group.edit_group_by_id(group, group_id)
    new_groups = db.get_group_list()
    old_groups[index].footer = group.footer
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
