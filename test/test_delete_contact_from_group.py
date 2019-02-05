import random

from model.contact import Contact
from model.group import Group


def test_delete_contact_from_group(app, db, db_orm):
    # создаем новый контакт
    app.contact.create(
        Contact(first_name="created_first_name", middle_name="created_middle_name", last_name="created_last_name"))
    # список контактов из БД
    old_contacts = db.get_contact_list()
    # берем рандомный контакт
    contact = random.choice(old_contacts)
    contact_id = contact.id
    # создаем новую группу
    app.group.create(
        Group(name="created group", footer="created logo of group", header="created comment for group"))
    # список групп из БД
    old_groups = db.get_group_list()
    # берем рандомную группу
    group = random.choice(old_groups)
    group_id = group.id
    # добавляем контакт в группу
    app.contact.add_to_group_by_id(contact_id, group_id)
    # удаляем контакт из группы
    app.contact.remove_from_group_by_id(contact_id)
    is_contact_in_group = False
    # проверяем что в контакт удалился из группы
    contacts_not_in_group = db_orm.get_contacts_not_in_group(group)
    for item in range(len(contacts_not_in_group)):
        if contacts_not_in_group[item].id == contact_id:
            is_contact_in_group = True

    assert is_contact_in_group == True
