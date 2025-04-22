while True:
    if not todo_list:
        print("Your ToDo list is empty")
    else:
        index = 1

    for task in todo_list:
        print(f"{index}. {task}")
        index += 1

    print("Options:")
    print("1) Add Task")
    print("2) Remove Task")
    print("3) Quit")
    
    choice = input("Which task? 1,2 or 3?")
    
    if choice == "1":
        choice = input("What task?")
        todo_list.append(choice)
        print("Adding task")
    elif choice == "2":
        todo_list.pop()
        print("Removing Task")
        print(todo_list)
    elif choice == "3":
        print("Quitting")
        break