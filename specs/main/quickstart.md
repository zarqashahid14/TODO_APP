# Quickstart Guide: Phase 1 Todo CLI App

**Feature**: Phase 1 - Todo CLI App
**Date**: 2026-01-01

---

## Prerequisites

- Python 3.11 or higher
- No external dependencies required (standard library only)
- Terminal or command prompt access

---

## Installation

### Step 1: Verify Python Version

```bash
python --version
# Should show: Python 3.11.x or higher
```

### Step 2: Download the Application

The application is a single file: `todo.py`

Place `todo.py` in your desired directory (e.g., `/home/user/todo-app/`)

---

## Running the Application

### Start the App

```bash
python todo.py
```

You should see the main menu:

```
=== Todo Manager ===
1. Add Todo
2. View Todos
3. Complete Todo
4. Delete Todo
5. Exit

Enter your choice (1-5):
```

---

## Basic Usage

### Adding Your First Todo

1. Enter `1` and press Enter
2. Enter a description when prompted (e.g., "Buy groceries")
3. The todo is added with ID 1

**Example**:
```
Enter your choice (1-5): 1
Enter todo description: Buy groceries
Todo added successfully! (ID: 1)
```

---

### Viewing All Todos

1. Enter `2` and press Enter
2. See a list of all your todos with IDs and status

**Example**:
```
Enter your choice (1-5): 2
=== Your Todos ===
1. [pending] Buy groceries
2. [pending] Walk the dog
```

---

### Marking a Todo as Complete

1. Enter `3` and press Enter
2. Enter the todo ID you want to complete
3. The todo status changes to "completed"

**Example**:
```
Enter your choice (1-5): 3
Enter todo ID to complete: 1
Todo #1 marked as completed!
```

Now view todos again to see the status change:
```
Enter your choice (1-5): 2
=== Your Todos ===
1. [completed] Buy groceries
2. [pending] Walk the dog
```

---

### Deleting a Todo

1. Enter `4` and press Enter
2. Enter the todo ID you want to delete
3. The todo is removed from your list

**Example**:
```
Enter your choice (1-5): 4
Enter todo ID to delete: 2
Todo #2 deleted successfully!
```

---

### Exiting the Application

1. Enter `5` and press Enter
2. The application closes

**Example**:
```
Enter your choice (1-5): 5
Goodbye!
```

---

## Common Scenarios

### Creating Multiple Todos

```
Enter your choice (1-5): 1
Enter todo description: Buy groceries
Todo added successfully! (ID: 1)

Enter your choice (1-5): 1
Enter todo description: Walk the dog
Todo added successfully! (ID: 2)

Enter your choice (1-5): 1
Enter todo description: Call mom
Todo added successfully! (ID: 3)

Enter your choice (1-5): 2
=== Your Todos ===
1. [pending] Buy groceries
2. [pending] Walk the dog
3. [pending] Call mom
```

---

### Managing Completed Todos

```
# Add todos
Enter your choice (1-5): 1
Enter todo description: Task A
Todo added successfully! (ID: 1)

Enter your choice (1-5): 1
Enter todo description: Task B
Todo added successfully! (ID: 2)

# Complete one
Enter your choice (1-5): 3
Enter todo ID to complete: 1
Todo #1 marked as completed!

# View todos
Enter your choice (1-5): 2
=== Your Todos ===
1. [completed] Task A
2. [pending] Task B

# Delete the completed one
Enter your choice (1-5): 4
Enter todo ID to delete: 1
Todo #1 deleted successfully!
```

---

## Error Handling Examples

### Invalid Menu Choice

```
Enter your choice (1-5): abc
Invalid choice. Please enter a number between 1 and 5.
```

```
Enter your choice (1-5): 99
Invalid choice. Please enter a number between 1 and 5.
```

---

### Empty Todo Description

```
Enter your choice (1-5): 1
Enter todo description:
Description cannot be empty.
Enter todo description: Walk the dog
Todo added successfully! (ID: 1)
```

```
Enter your choice (1-5): 1
Enter todo description:
(only spaces)
Description cannot be empty.
Enter todo description: Walk the dog
Todo added successfully! (ID: 1)
```

---

### Invalid Todo ID (Complete)

```
Enter your choice (1-5): 3
Enter todo ID to complete: abc
Please enter a valid number.
Enter todo ID to complete: 999
Invalid todo ID.
```

---

### Invalid Todo ID (Delete)

```
Enter your choice (1-5): 4
Enter todo ID to delete: abc
Please enter a valid number.
Enter todo ID to delete: 999
Invalid todo ID.
```

---

## Tips

1. **View todos frequently**: Use option 2 to see your list and check IDs
2. **IDs are stable**: Deleting a todo doesn't change other IDs (e.g., if you delete ID 2, ID 3 stays as ID 3)
3. **Data is not saved**: All todos are lost when you exit the app (normal for Phase 1)
4. **Special characters allowed**: You can use emojis, punctuation, and any text in descriptions
5. **Use Ctrl+C**: Press Ctrl+C to force-quit if needed (not recommended - use option 5)

---

## Troubleshooting

### "python: command not found"

**Solution**: Install Python 3.11 from [python.org](https://www.python.org/downloads/)

---

### "ModuleNotFoundError" (if you see this)

**Solution**: This shouldn't happen - Phase 1 uses only standard library. Verify you're using `python todo.py` and not importing from a different file.

---

### App crashes with unexpected error

**Solution**: Check that:
- Python version is 3.11 or higher (`python --version`)
- You're running the correct file (`python todo.py`)
- No file permissions issues (try `chmod +x todo.py` on Linux/Mac)

---

## Next Steps

After completing Phase 1 quickstart, refer to:

- **[spec.md](./spec.md)**: Full feature requirements and user stories
- **[plan.md](./plan.md)**: Technical architecture and design decisions
- **[data-model.md](./data-model.md)**: Data structures and entity definitions
- **[contracts/cli-interface.md](./contracts/cli-interface.md)**: Complete interface specification for testing

---

## Support

For issues or questions about Phase 1, consult:
- Constitution: `.specify/memory/constitution.md`
- Research: `specs/main/research.md`
- Spec: `specs/main/spec.md`
