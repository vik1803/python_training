from python_training.model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(name="Edited name"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(header="Edited header"))


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(header="Edited footer"))
