from sys import maxsize


class Group:

    def __init__(self, name=None, footer=None, header=None, id=None):
        self.name = name
        self.footer = footer
        self.header = header
        self.id = id

    def __repr__(self):
        return "Id: %s; Name: %s; Header: %s; Footer: %s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
