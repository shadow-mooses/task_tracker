myDict = [{1:"task one"},
          {2:"task two"},
          {5:"task five"},
          {3:"task three"}]

todo_list = [
    {'id':1,'task':'sleep'},
    {'id':2,'task':'nap'},
    {'id':12,'task':'go to sleep'}
]

todo_list2 = [
    {'id':1,'task':'sleep','status':'Not started'},
    {'id':2,'task':'nap','status':'Not started'},
    {'id':12,'task':'go to sleep','status':'Not started'}
            ]

empty_list = [
    {'id':0, 'task':None,'status':'Not started'}
]


#works - loops through the tasks, creates a dictionary with the task id and the list index. Then pops the index in the todo list.
#unused since delete API calls can't be done with flask?
def delete_task(task_num, list):
    task_list_dict = {}
    task_list_index = 0
    for dict in list: #loop through the todo list and create a dictionary of the task ids and the index in the list
        for value in dict.values():
            if type(value) == int:
                task_list_dict[value] = task_list_index
                task_list_index += 1
            else:
                break
    list.pop(task_list_dict[task_num])



#works
def new_max_key(list) -> list:
    key_list = []
    for dict in list:
        for value in dict.values():
            if type(value) == int:
                key_list.append(value)
            else:
                break
    return max(key_list) + 1


#del_task_num = int(input('which task to delete?'))

#works - loops through the tasks, creates a dictionary with the task id and the task/list index. Then pops the index in the todo list.
def delete_task(task_num, list):
    task_list_dict = {}
    task_list_index = 0
    for dict in list:
        for value in dict.values():
            if type(value) == int:
                task_list_dict[value] = task_list_index
                task_list_index += 1
            else:
                break
    list.pop(task_list_dict[task_num])
    return list
    
#this needs to loop through the list of dictionaries and update the status -> 'completed'
def task_completer(task_num, list):
    if type(task_num) == int:
        task_list_dict = {}
        task_list_index = 0
        for dict in list: #loop through the todo list and create a dictionary of the task ids and the index in the list
            for value in dict.values():
                if type(value) == int:
                    task_list_dict[value] = task_list_index
                    task_list_index += 1
                else:
                    break
        if task_num in task_list_dict:
            updated_dict = list[task_list_dict[task_num]]
            updated_dict['status'] = 'completed'
            return updated_dict
        raise KeyError('task_num is out of range')
    raise TypeError('task_num is not an integer')

def task_len_checker(list) -> list:
    list_plus = []
    if len(list) == 1:
        return print('your task list is empty')
    elif len(list) > 1:
        for task in len(list):
            
            list_plus.append(list[task] += 1)
    return list_plus


print(task_len_checker(empty_list))
            
