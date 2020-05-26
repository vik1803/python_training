# -*- coding: utf-8 -*-
from python_training.model.contact import Contact
import re


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
        self.open_contact_to_edit_by_index(index)
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
            self.app.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_xpath(".//input").get_attribute("value")
                surname = element.find_element_by_xpath("./*[2]").text
                name = element.find_element_by_xpath("./*[3]").text
                address = element.find_element_by_xpath("./*[4]").text
                all_emails = element.find_element_by_xpath("./*[5]").text
                all_phones = element.find_element_by_xpath("./*[6]").text
                self.contacts_cache.append(Contact(id=id, surname=surname, name=name, address=address,
                                                   all_emails=all_emails, all_phones_from_home_page=all_phones))
        return self.contacts_cache

    # def get_contact_list(self):
    #     if self.contacts_cache is None:
    #         wd = self.app.wd
    #         self.app.open_home_page()
    #         self.contacts_cache = []
    #         for row in wd.find_elements_by_name("entry"):
    #             cells = row.find_elements_by_tag_name("td")
    #             id = cells[0].find_element_by_tag_name("input").get_attribute("value")
    #             name = cells[1].text
    #             surname = cells[2].text
    #             all_phones = cells[5].text.splitlines()
    #             self.contacts_cache.append(Contact(id=id, name=name, surname=surname, home_phone=all_phones[0],
    #                                                mob_phone=all_phones[1], work_phone=all_phones[2],
    #                                                secondary_phone=all_phones[3]))
    #     return list(self.contacts_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Редагувати']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        surname = wd.find_element_by_name("lastname").get_attribute("value")
        name = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mob_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, surname=surname, name=name, address=address, email_1=email_1, email_2=email_2,
                       email_3=email_3, home_phone=home_phone, work_phone=work_phone, mob_phone=mob_phone,
                       secondary_phone=secondary_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mob_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mob_phone=mob_phone, secondary_phone=secondary_phone)
