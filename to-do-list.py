class TaskNode:
    def __init__(self, task):
        self.task = task
        self.next = None

class TodoList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_task = TaskNode(task)
        if not self.head:
            self.head = new_task
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_task
        print(f"Task '{task}' added.")

    def add_multiple_tasks(self):
        print("Enter tasks one by one. Press Enter without typing anything to stop.")
        while True:
            task = input("Enter task: ").strip()
            if not task:
                break
            self.add_task(task)

    def update_task(self, old_task, new_task):
        current = self.head
        while current:
            if current.task == old_task:
                current.task = new_task
                print(f"Task '{old_task}' updated to '{new_task}'.")
                return
            current = current.next
        print(f"Task '{old_task}' not found.")

    def delete_task(self, task):
        current = self.head
        if current and current.task == task:
            self.head = current.next
            print(f"Task '{task}' deleted.")
            return
        prev = None
        while current:
            if current.task == task:
                prev.next = current.next
                print(f"Task '{task}' deleted.")
                return
            prev, current = current, current.next
        print(f"Task '{task}' not found.")

    def display_tasks(self):
        if not self.head:
            print("No tasks in the list.")
            return
        current = self.head
        print("To-Do List:")
        while current:
            print(f"- {current.task}")
            current = current.next

def main():
    todo = TodoList()
    while True:
        print("\n-- To-Do List Menu --")
        print("1. Add Task")
        print("2. Add Multiple Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Display Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            task = input("Enter task to add: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("Task cannot be empty.")

        elif choice == '2':
            todo.add_multiple_tasks()

        elif choice == '3':
            old_task = input("Enter task to update: ").strip()
            new_task = input("Enter new task: ").strip()
            if old_task and new_task:
                todo.update_task(old_task, new_task)
            else:
                print("Both old and new tasks must be provided.")

        elif choice == '4':
            task = input("Enter task to delete: ").strip()
            if task:
                todo.delete_task(task)
            else:
                print("Task cannot be empty.")

        elif choice == '5':
            todo.display_tasks()

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option .")

if __name__ == "__main__":
    main()
