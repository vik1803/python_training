import re
from random import randrange
from python_training.model.contact import Contact


def clear(s):
    return re.sub("[() -]", "", s)


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mob_phone == contact_from_edit_page.mob_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.home_phone, contact.mob_phone, contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email_1, contact.email_2, contact.email_3])))


def test_contacts_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(name=''))
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.surname == contact_from_edit_page.surname
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
