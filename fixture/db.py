import mysql.connector
from python_training.model.group import Group
from python_training.model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(
            host=host,
            database=name,
            user=user,
            password=password,
            autocommit=True
        )

    def get_group_list(self):
        groups_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups_list

    def get_contact_list(self):
        contacts_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address from addressbook")
            for row in cursor:
                (id, name, surname, address) = row
                contacts_list.append(Contact(id=str(id), name=name, surname=surname, address=address))
        finally:
            cursor.close()
        return contacts_list

    def destroy(self):
        self.connection.close()
