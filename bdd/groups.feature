Scenario Outline: Add new group
Given a group list
Given group with <name>, <header> and <footer>
When I add the group to list
Then the new group list is equal to the old list with the added group

Examples:
| name | header | footer |
| name1 | header1 | footer1 |
| name2 | header2 | footer2 |


Scenario: Delete a group
Given a non-empty group list
Given a random group from list
When I delete a group from list
Then the new group list is equal to the old list without deleted group