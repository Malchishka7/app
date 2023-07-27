class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task_info in enumerate(self.tasks, start=1):
                status = "✓" if task_info["completed"] else " "
                print(f"{index}. [{status}] {task_info['task']}")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n== To-Do List ==")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
