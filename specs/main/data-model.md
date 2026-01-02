# Data Model: Phase 1 Todo CLI App

**Feature**: Phase 1 - Todo CLI App
**Date**: 2026-01-01
**Spec Reference**: [spec.md](./spec.md)

---

## Entities

### Todo

Represents a single task item in the todo list.

#### Fields

| Field Name | Type | Description | Constraints | Default |
|------------|------|-------------|-------------|---------|
| id | int | Unique identifier for the todo | Must be positive integer, stable across deletions | Auto-incrementing (1, 2, 3...) |
| description | str | Text description of the todo | Non-empty string after stripping whitespace | Required |
| status | str | Current completion state | Must be "pending" or "completed" | "pending" |

#### Validation Rules

1. **id**: Must be a positive integer (>= 1). Never re-used after deletion.
2. **description**: After `str.strip()`, must have length >= 1. Special characters allowed.
3. **status**: Only two valid values: `"pending"` or `"completed"`.

#### State Transitions

```
[pending] --(complete operation)--> [completed]
[completed] --(no valid operation to revert)--> [completed]
```

**Note**: Phase 1 does not support reverting to "pending". Once completed, stays completed.

---

## Data Structure

### In-Memory Storage

```python
# Python list of dictionaries
todos: list[dict] = [
    {
        'id': 1,
        'description': 'Buy groceries',
        'status': 'pending'
    },
    {
        'id': 2,
        'description': 'Walk the dog',
        'status': 'completed'
    }
]
```

### ID Counter

```python
next_id: int = 3  # Next ID to assign (IDs 1, 2 already used)
```

---

## Relationships

**No relationships in Phase 1** - Todos are independent items with no links between them.

---

## Operations

### Create (Add Todo)

**Input**: description (str)
**Output**: New todo dict with auto-generated id

```python
{
    'id': next_id,
    'description': description,
    'status': 'pending'
}
```

**Side Effect**: Increments `next_id` by 1

---

### Read (View All Todos)

**Input**: None
**Output**: List of all todo dicts

**Order**: Preserves insertion order (as stored in list)

---

### Update (Complete Todo)

**Input**: todo_id (int)
**Output**: Updated todo dict or None (if id not found)

**Side Effect**: Sets `status` to `"completed"` for the matching todo

---

### Delete (Remove Todo)

**Input**: todo_id (int)
**Output**: Deleted todo dict or None (if id not found)

**Side Effect**: Removes todo from list. Does **not** decrement `next_id`.

---

## Constraints & Invariants

1. **Uniqueness**: No two todos share the same `id` value.
2. **ID Stability**: Deleting a todo does not reuse its ID. IDs are monotonically increasing.
3. **Persistence**: None (Phase 1 only). All data lost when app exits.
4. **No Orphaned IDs**: IDs are sequential but may have gaps after deletions (e.g., 1, 3, 5 if 2 and 4 deleted).
5. **Order**: List order matches creation order. No sorting or reordering in Phase 1.

---

## Example Lifecycle

```python
# Initial state
todos = []
next_id = 1

# Add todo 1
todos.append({'id': 1, 'description': 'Task 1', 'status': 'pending'})
next_id = 2

# Add todo 2
todos.append({'id': 2, 'description': 'Task 2', 'status': 'pending'})
next_id = 3

# Complete todo 1
todos[0]['status'] = 'completed'  # todo id 1

# Delete todo 2
todos.pop(1)  # remove todo id 2
# next_id remains 3, not decremented

# Add todo 3
todos.append({'id': 3, 'description': 'Task 3', 'status': 'pending'})
next_id = 4

# Final state
todos = [
    {'id': 1, 'description': 'Task 1', 'status': 'completed'},
    {'id': 3, 'description': 'Task 3', 'status': 'pending'}
]
```

---

## Schema Evolution (Phase 2+)

**Planned but out of scope for Phase 1**:

- Add optional fields: `due_date`, `priority`, `tags`
- Add relationships: Subtasks, categories
- Add persistence: SQLite schema with migration support
- Add ordering: Custom sort orders, drag-and-drop reordering
