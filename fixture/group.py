from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_xpath("//li/a[text()='groups']").click()

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

    def edit_first_group(self, group):
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

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements_by_xpath("//span[@class='group']"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups
