# Feature Specification: Phase 1 - Todo CLI App

**Feature Branch**: `main`
**Created**: 2026-01-01
**Status**: Draft
**Input**: User description: "Create a technical plan for Phase 1. 1. Language: Python 3.11. 2. Architecture: TodoManager class for CRUD, and a main() function for the CLI loop. 3. Storage: Local list of dictionaries. 4. Error Handling: Try-except blocks for user input. Follow the Simplicity First rule from our constitution."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create New Todo (Priority: P1)

User can add a new todo item with a description to their todo list through the CLI.

**Why this priority**: This is the core functionality - without the ability to create todos, nothing else matters.

**Independent Test**: Can be fully tested by running the app, adding a todo via the CLI, and verifying it appears in the list.

**Acceptance Scenarios**:

1. **Given** the CLI is running, **When** user selects "Add Todo" and enters "Buy groceries", **Then** the todo is added with status "pending"
2. **Given** the CLI is running, **When** user selects "Add Todo" and enters an empty string, **Then** system displays error message and prompts again
3. **Given** the CLI is running, **When** user selects "Add Todo" and enters a valid description, **Then** the todo receives a unique ID (incrementing integer)

---

### User Story 2 - View All Todos (Priority: P1)

User can view all todo items in their list with ID, description, and status.

**Why this priority**: Users need to see what they've added to track their tasks.

**Independent Test**: Can be fully tested by adding multiple todos, then selecting "View Todos" and verifying all items display correctly.

**Acceptance Scenarios**:

1. **Given** 3 todos exist, **When** user selects "View Todos", **Then** all 3 todos display with ID, description, and status
2. **Given** no todos exist, **When** user selects "View Todos", **Then** system displays "No todos found" message
3. **Given** todos exist with mixed statuses, **When** user selects "View Todos", **Then** display shows status for each todo (pending/completed)

---

### User Story 3 - Mark Todo as Complete (Priority: P1)

User can mark an existing todo as completed by its ID.

**Why this priority**: Users need to track progress and mark items as done.

**Independent Test**: Can be fully tested by adding a todo, marking it complete, and viewing todos to confirm status changed.

**Acceptance Scenarios**:

1. **Given** a todo with ID 1 exists with status "pending", **When** user selects "Complete Todo" and enters ID 1, **Then** the todo status updates to "completed"
2. **Given** no todo with ID 99 exists, **When** user selects "Complete Todo" and enters ID 99, **Then** system displays "Invalid todo ID" error
3. **Given** a todo is already "completed", **When** user tries to complete it again, **Then** status remains "completed" (idempotent)

---

### User Story 4 - Delete Todo (Priority: P2)

User can delete a todo item from their list by its ID.

**Why this priority**: Users need to remove completed or cancelled tasks. This is P2 because users can work around by ignoring completed todos.

**Independent Test**: Can be fully tested by adding a todo, deleting it, and verifying it no longer appears in the list.

**Acceptance Scenarios**:

1. **Given** a todo with ID 1 exists, **When** user selects "Delete Todo" and enters ID 1, **Then** the todo is removed from the list
2. **Given** no todo with ID 99 exists, **When** user selects "Delete Todo" and enters ID 99, **Then** system displays "Invalid todo ID" error
3. **Given** 3 todos exist and ID 2 is deleted, **When** user views todos, **Then** only IDs 1 and 3 remain (IDs are stable, not re-used)

---

### Edge Cases

- What happens when user enters non-numeric input when selecting a todo ID?
- How does system handle special characters in todo descriptions?
- What happens when user enters invalid menu choice (not 1-5)?
- How does system handle whitespace-only input for todo descriptions?
- What happens when list is empty and user tries to complete/delete?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to create todo items with text descriptions
- **FR-002**: System MUST assign unique incrementing integer IDs to each todo (starting at 1)
- **FR-003**: System MUST maintain todo status as either "pending" or "completed"
- **FR-004**: System MUST display all todos with ID, description, and status in a numbered list
- **FR-005**: System MUST allow marking todos as completed by ID
- **FR-006**: System MUST allow deleting todos by ID
- **FR-007**: System MUST validate user input for menu selections (1-5 only)
- **FR-008**: System MUST validate user input for todo IDs (numeric and exists in list)
- **FR-009**: System MUST handle invalid input gracefully with error messages and re-prompt
- **FR-010**: System MUST provide continuous CLI loop until user chooses to exit

### Key Entities

- **Todo**: Represents a single task item with unique ID, text description, and status (pending/completed)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can create, view, complete, and delete todos without errors
- **SC-002**: CLI menu loop runs continuously until user selects "Exit" (menu option 5)
- **SC-003**: All invalid inputs are caught with try-except blocks and display clear error messages
- **SC-004**: Todo IDs remain stable (not re-used) after deletions
- **SC-005**: Zero crashes or unhandled exceptions during normal operation
