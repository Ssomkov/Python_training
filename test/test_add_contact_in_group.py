import random

import pytest

from model.contact import Contact
from model.group import Group


def test_add_contact_in_group(app, db, db_orm):
    # создаем новый контакт если контактов нет
    with pytest.allure.step('Create contact if not exists'):
        if app.contact.count() == 0:
            app.contact.create(
                Contact(first_name="created_first_name", middle_name="created_middle_name",
                        last_name="created_last_name"))
    # создаем группу если групп нет
    with pytest.allure.step('Create group if not exists'):
        if len(db.get_group_list()) == 0:
            app.group.create(
                Group(name="created group", footer="created logo of group", header="created comment for group"))
    # список групп из БД
    with pytest.allure.step('Get group list from DB'):
        old_groups = db.get_group_list()
    # берем рандомную группу
    with pytest.allure.step('Get random group'):
        group = random.choice(old_groups)
        group_id = group.id
    # берем контакты не входящие в эту группу
    with pytest.allure.step('Get contact not in group %s' % group):
        contacts_not_in_group = db_orm.get_contacts_not_in_group(group)
        contact = random.choice(contacts_not_in_group)
        contact_id = contact.id
    # добавляем контакт в группу
    with pytest.allure.step('Add contact in group'):
        app.contact.add_to_group_by_id(contact_id, group_id)
        is_contact_in_group = False
    # проверяем что в контакт добавился в группу
    with pytest.allure.step('Verify contact %s was added to group %s' % (contact, group)):
        contacts_in_group = db_orm.get_contacts_in_group(group)
        for item in range(len(contacts_in_group)):
            if contacts_in_group[item].id == contact_id:
                is_contact_in_group = True
        assert is_contact_in_group == True
