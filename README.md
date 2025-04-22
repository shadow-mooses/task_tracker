## Task Tracker v0.2
This is a basic task tracker web app that uses flask to organize routes or pages to create a general, simple task tracker.
## Function
This app allows users to populate a list of taks stored in memory with an index, description and status. A user can 'complete' a task by entering the task id number.

When a user logs out, the task list is saved as a JSON with a timestamp and the session cookie is removed from the browser.
## Site Map
- Main - This is the index page that defines the navbar and persistent title with the child block content at the end.
- Register - This is the block content that checks the username and password against the list of registered users. Registering with an approved user name and password sends a session cookie to the browser. Without the session cookie, a user is unable to log into history.
- Manage Tasks - This page has an input field where you add the description of the task. Add a description and the task history will be populated with a task id (integer) and a status (not started).
- It also includes a user input field to delete task by the 'task_id'. This is assigned at item creation in a key:value pair.
- Task History - this is a table of all tasks that have been created. It includes their task id, the description of the task and the status.
- Complete Task - add the task ID to update it's status from not started to complete. There is some error handling when a user enteres a string or an index that is out of bounds.