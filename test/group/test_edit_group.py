from python_training.model.group import Group


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="Edited name"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="Edited header"))


def test_edit_group_footer(app):
    app.group.edit_first_group(Group(header="Edited footer"))
