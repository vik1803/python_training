# -*- coding: utf-8 -*-
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
        wd = self.app.wd
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

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        # self.open_groups_page()
        self.select_first_contact()
        # Open selected contact
        wd.find_element_by_xpath("//img[@alt='Редагувати']").click()
        # Edit field
        self.fill_contact_form(new_contact_data)
        # Submit editing
        wd.find_element_by_xpath("//input[@value='Оновити']").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Видалити']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_xpath("//input[@value='Видалити']")

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))
