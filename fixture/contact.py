# -*- coding: utf-8 -*-
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Додати контакт").click()

    def add_new(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # Fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.surname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.addr)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mob_phone)
        # Submit contact form
        wd.find_element_by_xpath("//input[@name='submit']").click()
        # Return to add contact page
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # Select the first contact
        wd.find_element_by_name("selected[]").click()
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Видалити']").click()
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # Select the first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Редагувати']").click()
        # Edit selected contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.surname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.addr)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mob_phone)
        # Submit editing contact
        wd.find_element_by_xpath("//input[@value='Оновити']").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
