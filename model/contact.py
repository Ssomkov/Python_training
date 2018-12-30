from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None, title=None,
                 company=None, first_address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None, birthday_day=None, birthday_month=None,
                 birthday_year=None, anniversary_day=None, anniversary_month=None, anniversary_year=None, group=None,
                 secondary_address=None, secondary_phone=None, notes=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.first_address = first_address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.group = group
        self.secondary_address = secondary_address
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s %s %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
