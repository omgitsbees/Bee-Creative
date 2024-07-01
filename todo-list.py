# Define a dictionary to store tasks
tasks = {}

# Function to add a task
def add_task(task):
    tasks[len(tasks) + 1] = {'task': task, 'completed': False}

# Function to mark a task as completed
def complete_task(task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = True
    else:
        print("Task not found.")

# Function to display all tasks
def display_tasks():
    if tasks:
        print("Tasks:")
        for task_id, task_info in tasks.items():
            status = '✓' if task_info['completed'] else '✗'
            print(f"{task_id}. [{status}] {task_info['task']}")
    else:
        print("No tasks found.")

# Main function to run the to-do list application
def main():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            add_task(task)
            print("Task added!")

        elif choice == '2':
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(task_id)

        elif choice == '3':
            display_tasks()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
