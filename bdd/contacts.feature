Scenario Outline: Add new contact
Given a contact list
Given contact with <first_name>, <middle_name> and <last_name>
When I add the contact to list
Then the new contact list is equal to the old contact list with the added contact

Examples:
| first_name | middle_name | last_name |
| first_name1 | middle_name1 | last_name1 |
| first_name2 | middle_name12 | last_name2 |

Scenario: Delete contact
Given a non-empty contact list
Given a random contact from list
When I delete a contact from list
Then the new contact list is equal to the old list without deleted contact