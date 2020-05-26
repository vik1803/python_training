from sys import maxsize


class Contact:
    def __init__(self, id=None, name=None, surname=None, address=None, mob_phone=None, home_phone=None,
                 secondary_phone=None, work_phone=None, all_phones_from_home_page=None, email_1=None, email_2=None,
                 email_3=None, all_emails=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.address = address
        self.mob_phone = mob_phone
        self.home_phone = home_phone
        self.secondary_phone = secondary_phone
        self.work_phone = work_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.surname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.name == other.name and self.surname == other.surname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
