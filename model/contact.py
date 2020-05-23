from sys import maxsize


class Contact:
    def __init__(self, id=None, name=None, surname=None, address=None, mob_phone=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.address = address
        self.mob_phone = mob_phone

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.surname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.name == other.name
                and self.surname == other.surname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
