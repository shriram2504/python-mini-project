# Node class represents each task in the to-do list

class TaskNode:
    def __init__(self, task):
        self.task = task     # Stores the task description
        self.next = None     # Points to the next task (node)

# ToDoList class manages the linked list of tasks
class ToDoList:
    def __init__(self):
        self.head = None   # Initializes an empty list with no tasks

# Adds a new task to the end of the list
    def add_task(self, task):
        new_node = TaskNode(task)  # Creates a new node with the task
        if not self.head:          # If the list is empty
            self.head = new_node   # Set the new node as the head
        else:
            current = self.head
            while current.next:    # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Link the new node at the end
        print(f"Task '{task}' added successfully.")

 # Allows the user to add multiple tasks one by one
    def add_multiple_tasks(self):
        print("Enter tasks one by one. Press Enter without typing anything to stop.")
        while True:
            task = input("Enter task: ")
            if not task:                    # If the input is empty, stop adding tasks
                break
            self.add_task(task)

 # Updates an existing task with a new description
    def update_task(self, old_task, new_task):
        current = self.head
        while current:
            if current.task == old_task:   # If the task matches
                current.task = new_task    # Update the task description
                print(f"Task '{old_task}' updated to '{new_task}'.")
                return
            current = current.next
        print(f"Task '{old_task}' not found.")

 # Removes a task from the list
    def remove_task(self, task):
        current = self.head      
        if current and current.task == task:  # If the task is at the head
            self.head = current.next           # Remove the head node
            print(f"Task '{task}' removed successfully.")
            return
        prev = None
        while current:
            if current.task == task:         # If the task matches
                prev.next = current.next     # Bypass the current node
                print(f"Task '{task}' removed successfully.")
                return
            prev, current = current, current.next
        print(f"Task '{task}' not found.")

 # Displays all tasks with their corresponding node numbers
    def display_tasks(self):
        if not self.head:   # If the list is empty
            print("No tasks in the list.")
            return
        current = self.head
        print("To-Do List:")
        node_number = 1
        while current:
            print(f"Node {node_number}: {current.task}")   # Display node number and task
            current = current.next
            node_number += 1

# Main function to interact with the user
def main():
    todo_list = ToDoList()
    while True:
        print("\nMenu:")
        print("1. Add Multiple Tasks")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.add_multiple_tasks()
        elif choice == '2':
            old_task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            todo_list.update_task(old_task, new_task)
        elif choice == '3':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
