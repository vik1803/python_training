# -*- coding: utf-8 -*-
from python_training.model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/edit.php') and len(wd.find_elements_by_xpath("//input[@name='submit']")) > 0):
            wd.find_element_by_link_text(u"Додати контакт").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        # wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.surname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mob_phone)

    def add_new(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # Fill contact form
        self.fill_contact_form(contact)
        # Submit group creation
        wd.find_element_by_xpath("//input[@name='submit']").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)
        self.contacts_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Видалити']").click()
        wd.switch_to.alert.accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.contacts_cache = None

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(new_contact_data, 0)
        self.contacts_cache = None

    def edit_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        # Open selected contact by index
        wd.find_elements_by_xpath("//img[@alt='Редагувати']")[index].click()
        # Edit field
        self.fill_contact_form(new_contact_data)
        # Submit editing
        wd.find_element_by_xpath("//input[@value='Оновити']").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.contacts_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_xpath(".//input").get_attribute("value")
                name = element.find_element_by_xpath("./*[3]").text
                surname = element.find_element_by_xpath("./*[2]").text
                self.contacts_cache.append(Contact(id=id, name=name, surname=surname))
        return self.contacts_cache
