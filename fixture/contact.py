from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and wd.find_element_by_xpath(
                "//input[@name='searchstring']").is_displayed()):
            wd.find_element_by_xpath("//div[@id='nav']//a[text()='home']").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.set_fields(contact)
        wd.find_element_by_xpath("//input[@value='Enter'][2]").click()
        self.contact_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contacts_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_by_index(0)
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//input[@name='selected[]']")[index].click()

    def edit_first_contact(self, contact):
        self.edit_by_index(0, contact)
        self.contact_cache = None

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_xpath("//a[contains(@href,'edit.php?id')]")[index].click()
        self.set_fields(contact)
        wd.find_element_by_xpath("//input[@value='Update'][2]").click()
        self.contact_cache = None

    def set_fields(self, contact):
        wd = self.app.wd
        self.set_text_field("firstname", contact.first_name)
        self.set_text_field("middlename", contact.middle_name)
        self.set_text_field("lastname", contact.last_name)
        self.set_text_field("nickname", contact.nick_name)
        self.set_text_field("title", contact.title)
        self.set_text_field("company", contact.company)
        self.set_text_field("address", contact.first_address)
        self.set_text_field("home", contact.home_phone)
        self.set_text_field("mobile", contact.mobile_phone)
        self.set_text_field("work", contact.work_phone)
        self.set_text_field("fax", contact.fax)
        self.set_text_field("email", contact.email)
        self.set_text_field("email2", contact.email2)
        self.set_text_field("email3", contact.email3)
        self.set_text_field("homepage", contact.homepage)
        self.set_dropdown_field("bday", contact.birthday_day)
        self.set_dropdown_field("bmonth", contact.birthday_month)
        self.set_text_field("byear", contact.birthday_year)
        self.set_dropdown_field("aday", contact.anniversary_day)
        self.set_dropdown_field("amonth", contact.anniversary_month)
        self.set_text_field("ayear", contact.anniversary_year)
        self.set_dropdown_field("new_group", contact.group)
        self.set_text_field("address2", contact.secondary_address)
        self.set_text_field("phone2", contact.secondary_home)
        self.set_text_field("notes", contact.notes)

    def set_text_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def set_dropdown_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            element: WebElement
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                elements = element.find_elements_by_tag_name("td")
                first_name = elements[2].text
                last_name = elements[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name))
        return list(self.contact_cache)
