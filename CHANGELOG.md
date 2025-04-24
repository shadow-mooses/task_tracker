## v0.2
- Routes completed
- Functions tested

## v0.8
- Modified the todo list dictionary to include an 'id' key, value pair instead of just an integer and a 'task' description.
- Updated the functions and loops accordingly to account for this change.
- Able to populate the todo list with the description and iterating over the task id to aggregate and find the max value in the list. Then incrementing by one to add the new list. 

## v1.0
- Pivoted from removing (deleting) the task in the todo list to updating a status (key, value pair). This was the final goal to complete the app.
- The task_completer function has the same loop, iteration over the dicitonary. Loops over the task ids, adds them to a new dictionary with a index of the list. Then updates the 'status' value from 'not started' to complete.
- Added error handling for the task complete function.


## v1.2
- fixed the zero index task displayed in history
- fixed error handling for compeleting tasks or trying to add a string instead of an integer
- task complete successfully works
- added a quick line instead of displaying the zero index empty task

## Need to add for v1.5
- Add task table to the task_complete route so a user doesn't have to refer back to the table.
- try the back button on the task_complete route or add the top nav.
- Add more fields to the todo list like a timestamp that it was added and the timestamp when it was completed.
- restrict the task history to check if the user has logged in.
- load previous json tasks