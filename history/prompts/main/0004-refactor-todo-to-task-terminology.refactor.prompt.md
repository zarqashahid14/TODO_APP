---
id: 0004
title: Refactor Todo to Task terminology
stage: refactor
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: main
branch: main
user: user
command: /sp.implement
labels: ["refactor","terminology","user-facing-text"]
links:
  spec: /specs/main/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - todo.py (modified - user-facing text updated)
tests:
  - Manual CLI testing - verified new terminology displays correctly
---

## Prompt

/sp.implement "In todo.py, rename all occurrences of 'Todo' to 'Task' in the menu and messages. For example, 'Add Todo' should become 'Add Task' and 'View Todos' should become 'View Tasks'. Ensure the user-facing text is consistent."

## Response snapshot

Refactored all user-facing text in todo.py to use "Task" terminology instead of "Todo":

**Changes Made**:

1. **Menu Header**: "=== Todo Manager ===" → "=== Task Manager ==="

2. **Menu Options**:
   - "1. Add Todo" → "1. Add Task"
   - "2. View Todos" → "2. View Tasks"
   - "3. Complete Todo" → "3. Complete Task"
   - "4. Delete Todo" → "4. Delete Task"

3. **Add Function**:
   - Prompt: "Enter todo description: " → "Enter task description: "
   - Success: "Todo added successfully!" → "Task added successfully!"
   - Docstring: Updated to reference "Task" instead of "Todo"

4. **View Function**:
   - Empty state: "No todos found. Add some todos to get started!" → "No tasks found. Add some tasks to get started!"
   - Header: "=== Your Todos ===" → "=== Your Tasks ==="
   - Docstring: Updated to reference "Tasks" instead of "Todos"

5. **Complete Function**:
   - Prompt: "Enter todo ID to complete: " → "Enter task ID to complete: "
   - Success: "Todo #{id} marked as completed!" → "Task #{id} marked as completed!"
   - Error: "Invalid todo ID." → "Invalid task ID."
   - Docstring: Updated to reference "task ID" instead of "todo ID"

6. **Delete Function**:
   - Prompt: "Enter todo ID to delete: " → "Enter task ID to delete: "
   - Success: "Todo #{id} deleted successfully!" → "Task #{id} deleted successfully!"
   - Error: "Invalid todo ID." → "Invalid task ID."
   - Docstring: Updated to reference "task ID" instead of "todo ID"

**What Was NOT Changed**:
- Internal variable names (e.g., `todo`, `todos`, `todo_id`) kept as-is for code consistency
- Class name `TodoManager` kept as-is (internal implementation detail)
- Method names (e.g., `add_todo`, `complete_todo`) kept as-is (internal API)
- File name `todo.py` unchanged

**Verification**: Tested with `echo -e "2\n5" | python3 todo.py` - confirmed new terminology displays correctly.

## Outcome

- ✅ Impact: All user-facing text consistently uses "Task" terminology instead of "Todo"
- 🧪 Tests: Manual CLI testing PASS - menu and messages display correctly
- 📁 Files: todo.py (6 functions updated with new terminology)
- 🔁 Next prompts: Ready for git commit or additional features
- 🧠 Reflection: Clean refactor maintaining internal consistency while improving user-facing terminology. All print statements and input prompts updated without breaking functionality.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Manual validation PASS
- Prompt variant (if applicable): Direct refactoring approach
- Next experiment (smallest change to try): None - refactoring complete
