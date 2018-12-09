class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li/a[text()='groups']").click()

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_xpath("//li/a[text()='groups']").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def delete(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        wd.find_element_by_xpath("//input[@name='delete'][1]").click()

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        wd.find_element_by_xpath("//input[@name='edit'][1]").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.open_groups_page()
