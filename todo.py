#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Todo CLI Application - Phase 1
A simple command-line todo application following Simplicity First principle.

Author: Phase 1 Implementation
Date: 2026-01-01
"""


class TodoManager:
    """
    Manages a list of todo items with CRUD operations.

    Attributes:
        todos (list[dict]): List of todo dictionaries with id, description, status
        next_id (int): Counter for generating unique todo IDs
    """

    def __init__(self):
        """Initialize TodoManager with empty todo list and ID counter starting at 1."""
        self.todos: list[dict] = []
        self.next_id: int = 1

    def add_todo(self, description: str) -> dict:
        """
        Add a new todo with the given description.

        Args:
            description (str): Text description of the todo item

        Returns:
            dict: The created todo dictionary

        Raises:
            ValueError: If description is empty after stripping whitespace
        """
        if not description or not description.strip():
            raise ValueError("Description cannot be empty.")

        todo = {
            'id': self.next_id,
            'description': description.strip(),
            'status': 'pending'
        }
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def list_todos(self) -> list[dict]:
        """
        Return all todos in the list.

        Returns:
            list[dict]: List of all todo dictionaries
        """
        return self.todos

    def complete_todo(self, todo_id: int) -> bool:
        """
        Mark a todo as completed by its ID.

        Args:
            todo_id (int): The ID of the todo to mark as completed

        Returns:
            bool: True if todo was found and completed, False otherwise
        """
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['status'] = 'completed'
                return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id (int): The ID of the todo to delete

        Returns:
            bool: True if todo was found and deleted, False otherwise
        """
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                self.todos.pop(i)
                return True
        return False


def display_menu():
    """
    Display the main menu with numbered options.

    Returns:
        None: This function only prints to console
    """
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print()


def handle_add_todo(manager):
    """
    Handle the "Add Task" menu option.

    Prompts user for description, validates input, and adds task.

    Args:
        manager (TodoManager): The TodoManager instance

    Returns:
        None
    """
    while True:
        description = input("Enter task description: ")

        try:
            todo = manager.add_todo(description)
            print(f"Task added successfully! (ID: {todo['id']})")
            break
        except ValueError as e:
            print(str(e))


def handle_view_todos(manager):
    """
    Handle the "View Tasks" menu option.

    Displays all tasks with ID, description, and status.

    Args:
        manager (TodoManager): The TodoManager instance

    Returns:
        None
    """
    todos = manager.list_todos()

    if not todos:
        print("No tasks found. Add some tasks to get started!")
    else:
        print("=== Your Tasks ===")
        for todo in todos:
            print(f"{todo['id']}. [{todo['status']}] {todo['description']}")


def handle_complete_todo(manager):
    """
    Handle the "Complete Task" menu option.

    Prompts user for task ID and marks it as completed.

    Args:
        manager (TodoManager): The TodoManager instance

    Returns:
        None
    """
    while True:
        try:
            todo_id = int(input("Enter task ID to complete: "))
            if manager.complete_todo(todo_id):
                print(f"Task #{todo_id} marked as completed!")
                break
            else:
                print("Invalid task ID.")
                return
        except ValueError:
            print("Please enter a valid number.")


def handle_delete_todo(manager):
    """
    Handle the "Delete Task" menu option.

    Prompts user for task ID and deletes it.

    Args:
        manager (TodoManager): The TodoManager instance

    Returns:
        None
    """
    while True:
        try:
            todo_id = int(input("Enter task ID to delete: "))
            if manager.delete_todo(todo_id):
                print(f"Task #{todo_id} deleted successfully!")
                break
            else:
                print("Invalid task ID.")
                return
        except ValueError:
            print("Please enter a valid number.")


def main():
    """
    Main application loop that displays menu and handles user choices.

    The loop continues until user selects option 5 (Exit).
    All user input is wrapped in try-except for error handling.
    """
    manager = TodoManager()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue

            # Handle menu options
            if choice == 1:
                handle_add_todo(manager)
            elif choice == 2:
                handle_view_todos(manager)
            elif choice == 3:
                handle_complete_todo(manager)
            elif choice == 4:
                handle_delete_todo(manager)
            elif choice == 5:
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
