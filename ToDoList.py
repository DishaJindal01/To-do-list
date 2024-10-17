def add_task(tasks, task):
    tasks.append(task)
    print("Added task:", task)


def view_tasks(tasks):
    if not tasks:
        print('No tasks in the list.')
    else:
        for idx, task in enumerate(tasks, start=1):
            print(idx,task)

def remove_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print("Removed task:",removed_task)
    else:
        print('Invalid task number.')


def main():
    tasks = []

    while True:
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Remove Task')
        print('4. Exit')
        choice = input('Choose an option: ')
        
        if choice == '1':
            task = input('Enter task: ')
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_number = int(input('Enter task number to remove: '))
            remove_task(tasks, task_number)
        elif choice == '4':
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    main()
