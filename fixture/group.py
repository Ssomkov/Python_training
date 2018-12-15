class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li/a[text()='groups']").click()
        x = 4

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath("//input[@name='new'][1]").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def delete(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_xpath("//input[@name='delete'][1]").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='selected[]']").click()

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_xpath("//input[@name='edit'][1]").click()
        self.fill_group_form(group)
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.open_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.set_text_field("group_name", group.name)
        self.set_text_field("group_header", group.header)
        self.set_text_field("group_footer", group.footer)

    def set_text_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)
