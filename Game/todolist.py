def todo_list():
    tasks = []
    
    while True:
        print("\n1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nYour To-Do List:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        elif choice == '2':
            task = input("Enter task to add: ")
            tasks.append(task)
            print(f"'{task}' has been added to the list.")
        elif choice == '3':
            task_num = int(input("Enter task number to remove: "))
            if 0 < task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' has been removed from the list.")
            else:
                print("Invalid task number!")
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

todo_list()