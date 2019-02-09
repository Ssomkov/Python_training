import random

from model.contact import Contact
from model.group import Group


def test_add_contact_in_group(app, db, db_orm):
    # создаем новый контакт если контактов нет
    if app.contact.count() == 0:
        app.contact.create(
            Contact(first_name="created_first_name", middle_name="created_middle_name", last_name="created_last_name"))
    # создаем группу если групп нет
    if len(db.get_group_list()) == 0:
        app.group.create(
            Group(name="created group", footer="created logo of group", header="created comment for group"))
    # список групп из БД
    old_groups = db.get_group_list()
    # берем рандомную группу
    group = random.choice(old_groups)
    group_id = group.id
    # берем контакты не входящие в эту группу
    contacts_not_in_group = db_orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_in_group)
    contact_id = contact.id
    # добавляем контакт в группу
    app.contact.add_to_group_by_id(contact_id, group_id)
    is_contact_in_group = False
    # проверяем что в контакт добавился в группу
    contacts_in_group = db_orm.get_contacts_in_group(group)
    for item in range(len(contacts_in_group)):
        if contacts_in_group[item].id == contact_id:
            is_contact_in_group = True

    assert is_contact_in_group == True
