# -*- coding: utf-8 -*-
from selenium import webdriver
from python_training.fixture.session import SessionHelper
from python_training.fixture.group import GroupHelper
from python_training.fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook")

    def destroy(self):
        self.wd.quit()