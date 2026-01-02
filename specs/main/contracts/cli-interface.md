# CLI Interface Contract: Phase 1 Todo App

**Feature**: Phase 1 - Todo CLI App
**Date**: 2026-01-01

---

## Overview

This contract defines the interactive CLI menu interface for the Phase 1 todo application. The CLI runs in a continuous loop until the user chooses to exit.

---

## Menu Interface

### Main Menu Display

The CLI displays a numbered menu with 5 options:

```
=== Todo Manager ===
1. Add Todo
2. View Todos
3. Complete Todo
4. Delete Todo
5. Exit

Enter your choice (1-5):
```

**Constraints**:
- Menu options are always 1-5
- User input must be validated as integer between 1-5
- Invalid input displays error and re-prompts

---

## Contract 1: Add Todo

### User Action
- Select menu option **1** (Add Todo)
- Enter a text description when prompted

### Input Format

```
Enter todo description: [string]
```

**Prompt**: `"Enter todo description: "`

**Input**: Any string (including special characters)

**Validation Rules**:
1. Input must be non-empty after `str.strip()`
2. If empty or whitespace-only, display error: `"Description cannot be empty."`
3. Re-prompt until valid input received

### Success Response

```
Todo added successfully! (ID: {id})
```

**Where `{id}` is the auto-generated todo ID (integer)**

### Error Responses

| Condition | Error Message | Recovery |
|-----------|---------------|----------|
| Empty input | `"Description cannot be empty."` | Re-prompt for description |

---

## Contract 2: View Todos

### User Action
- Select menu option **2** (View Todos)
- No further input required

### Input Format

No input. Displays current state of todo list.

### Success Response (Todos Exist)

```
=== Your Todos ===
1. [pending] {description}
2. [completed] {description}
3. [pending] {description}
...
```

**Format**:
- Each todo on separate line
- Format: `"{id}. [{status}] {description}"`
- Status wrapped in square brackets: `[pending]` or `[completed]`
- Display order matches insertion order (list order)

### Success Response (No Todos)

```
No todos found. Add some todos to get started!
```

### Error Responses

None (no input to validate)

---

## Contract 3: Complete Todo

### User Action
- Select menu option **3** (Complete Todo)
- Enter a todo ID to mark as completed

### Input Format

```
Enter todo ID to complete: [integer]
```

**Prompt**: `"Enter todo ID to complete: "`

**Input**: Integer (todo ID)

**Validation Rules**:
1. Input must be integer (validate with try-except)
2. ID must exist in todo list
3. If invalid, display error: `"Invalid todo ID."`

### Success Response

```
Todo #{id} marked as completed!
```

### Error Responses

| Condition | Error Message | Recovery |
|-----------|---------------|----------|
| Non-integer input | `"Please enter a valid number."` | Re-prompt for ID |
| ID not found | `"Invalid todo ID."` | Return to main menu |

---

## Contract 4: Delete Todo

### User Action
- Select menu option **4** (Delete Todo)
- Enter a todo ID to delete

### Input Format

```
Enter todo ID to delete: [integer]
```

**Prompt**: `"Enter todo ID to delete: "`

**Input**: Integer (todo ID)

**Validation Rules**:
1. Input must be integer (validate with try-except)
2. ID must exist in todo list
3. If invalid, display error: `"Invalid todo ID."`

### Success Response

```
Todo #{id} deleted successfully!
```

### Error Responses

| Condition | Error Message | Recovery |
|-----------|---------------|----------|
| Non-integer input | `"Please enter a valid number."` | Re-prompt for ID |
| ID not found | `"Invalid todo ID."` | Return to main menu |

---

## Contract 5: Exit Application

### User Action
- Select menu option **5** (Exit)
- No further input required

### Input Format

No input. Terminates the application.

### Success Response

```
Goodbye!
```

**Behavior**: Application exits (main loop terminates)

### Error Responses

None

---

## Error Handling Contracts

### Invalid Menu Choice

**Condition**: User enters value outside 1-5 (including non-integer)

**Response**:
```
Invalid choice. Please enter a number between 1 and 5.
```

**Recovery**: Re-display menu and prompt again

---

## Input Validation Summary

| Input Type | Validation Method | Valid Range/Format |
|------------|-------------------|-------------------|
| Menu choice | `int()` with try-except | 1-5 inclusive |
| Todo ID (complete/delete) | `int()` with try-except | Must exist in list |
| Todo description | `str.strip()` and length check | Non-empty after strip |

---

## Example Session

```
=== Todo Manager ===
1. Add Todo
2. View Todos
3. Complete Todo
4. Delete Todo
5. Exit

Enter your choice (1-5): 1
Enter todo description: Buy groceries
Todo added successfully! (ID: 1)

=== Todo Manager ===
1. Add Todo
2. View Todos
3. Complete Todo
4. Delete Todo
5. Exit

Enter your choice (1-5): 1
Enter todo description: Walk the dog
Todo added successfully! (ID: 2)

=== Todo Manager ===
1. Add Todo
2. View Todos
3. Complete Todo
4. Delete Todo
5. Exit

Enter your choice (1-5): 2
=== Your Todos ===
1. [pending] Buy groceries
2. [pending] Walk the dog

=== Todo Manager ===
1. Add Todo
2. View Todos
3. Complete Todo
4. Delete Todo
5. Exit

Enter your choice (1-5): 3
Enter todo ID to complete: 1
Todo #1 marked as completed!

=== Todo Manager ===
1. Add Todo
2. View Todos
3. Complete Todo
4. Delete Todo
5. Exit

Enter your choice (1-5): 5
Goodbye!
```

---

## Implementation Requirements

1. **All prompts must match exactly** (for automated testing in future phases)
2. **All error messages must match exactly**
3. **Menu loop must be infinite** until option 5 selected
4. **All user input must be wrapped in try-except** (per constitution FR-009)
5. **Whitespace handling**: All text input must use `str.strip()` before validation
6. **Case sensitivity**: Menu choices are numeric (case not applicable)
