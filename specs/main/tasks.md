# Tasks: Phase 1 - Todo CLI App

**Input**: Design documents from `/specs/main/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/cli-interface.md

**Tests**: No automated tests for Phase 1 - manual CLI testing per plan.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: Single file at repository root (todo.py)
- **No src/ directory** - Simplicity First principle
- **No tests/ directory** - Manual CLI testing only for Phase 1

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create todo.py file with shebang and encoding declaration in /mnt/d/hackathon-2-todo/phase-1/todo.py

**Checkpoint**: Project structure ready - todo.py file created

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T002 Implement TodoManager class __init__ method with todos list and next_id counter in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T003 Implement menu display function with 5 numbered options in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T004 Implement main function with menu loop skeleton in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T005 Implement menu choice validation (1-5) with try-except in /mnt/d/hackathon-2-todo/phase-1/todo.py

**Checkpoint**: Foundation ready - TodoManager class and CLI loop structure in place, user story implementation can now begin

---

## Phase 3: User Story 1 - Create New Todo (Priority: P1) 🎯 MVP

**Goal**: Users can add todo items with descriptions through the CLI

**Independent Test**: Run the app, select "Add Todo" (option 1), enter a description like "Buy groceries", verify todo is added with status "pending" and unique ID

### Implementation for User Story 1

- [X] T006 [US1] Implement TodoManager.add_todo method with description validation in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T007 [US1] Implement CLI handler for Add Todo option with description prompt and validation in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T008 [US1] Add error handling for empty description input (with re-prompt) in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T009 [US1] Integrate Add Todo handler into main menu loop in /mnt/d/hackathon-2-todo/phase-1/todo.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently - users can create todos

---

## Phase 4: User Story 2 - View All Todos (Priority: P1)

**Goal**: Users can view all todo items with ID, description, and status

**Independent Test**: Add multiple todos, select "View Todos" (option 2), verify all todos display correctly with ID, description, and status (pending/completed)

### Implementation for User Story 2

- [X] T010 [US2] Implement TodoManager.list_todos method returning all todos in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T011 [US2] Implement CLI handler for View Todos option with formatted display in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T012 [US2] Add "No todos found" message when list is empty in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T013 [US2] Format todo display as "{id}. [{status}] {description}" in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T014 [US2] Integrate View Todos handler into main menu loop in /mnt/d/hackathon-2-todo/phase-1/todo.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - users can create and view todos

---

## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P1)

**Goal**: Users can mark existing todos as completed by ID

**Independent Test**: Add a todo, select "Complete Todo" (option 3), enter the todo ID, view todos again to confirm status changed to "completed"

### Implementation for User Story 3

- [X] T015 [US3] Implement TodoManager.complete_todo method with ID validation in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T016 [US3] Implement CLI handler for Complete Todo option with ID prompt and validation in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T017 [US3] Add try-except for non-integer ID input with re-prompt in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T018 [US3] Add error handling for non-existent todo ID in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T019 [US3] Add idempotent behavior (already completed todos stay completed) in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T020 [US3] Integrate Complete Todo handler into main menu loop in /mnt/d/hackathon-2-todo/phase-1/todo.py

**Checkpoint**: All P1 stories should now be independently functional - users can create, view, and complete todos (MVP complete!)

---

## Phase 6: User Story 4 - Delete Todo (Priority: P2)

**Goal**: Users can delete todo items by ID

**Independent Test**: Add a todo, select "Delete Todo" (option 4), enter the todo ID, view todos to confirm it's removed and IDs remain stable

### Implementation for User Story 4

- [X] T021 [US4] Implement TodoManager.delete_todo method with ID validation in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T022 [US4] Implement CLI handler for Delete Todo option with ID prompt and validation in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T023 [US4] Add try-except for non-integer ID input with re-prompt in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T024 [US4] Add error handling for non-existent todo ID in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T025 [US4] Ensure IDs remain stable (do not reuse deleted IDs) in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T026 [US4] Integrate Delete Todo handler into main menu loop in /mnt/d/hackathon-2-todo/phase-1/todo.py

**Checkpoint**: All user stories should now be independently functional - users can create, view, complete, and delete todos

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final application polish

- [X] T027 Implement Exit option (option 5) with "Goodbye!" message in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T028 Add __main__ guard to allow running todo.py as module or script in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T029 Add docstrings to TodoManager class and all methods in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T030 Validate all prompts and error messages match contracts/cli-interface.md exactly in /mnt/d/hackathon-2-todo/phase-1/todo.py
- [X] T031 Run quickstart.md validation to ensure all scenarios work as documented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1 - Create)**: Can start after Foundational - No dependencies on other stories
- **User Story 2 (P1 - View)**: Can start after Foundational - No dependencies on other stories
- **User Story 3 (P1 - Complete)**: Can start after Foundational - Depends on US1 (needs todos to exist)
- **User Story 4 (P2 - Delete)**: Can start after Foundational - Depends on US1 (needs todos to exist)

**Note**: While US3 and US4 depend on US1 (need todos to exist), they are functionally independent operations once todos are created. Each can be tested independently by first creating a todo.

### Within Each User Story

- Models before CLI handlers (within the same file)
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

**Limited parallelism in Phase 1** due to single-file architecture (Simplicity First principle):

- Once Foundational phase (Phase 2) completes, all user stories can be worked on in parallel by different team members
- However, within each story, tasks are mostly sequential due to single-file nature
- Only truly parallel tasks would be separate features being developed by different people

---

## Parallel Example: User Story 1

```python
# Limited parallelism in single-file architecture
# Tasks T006-T009 must be done sequentially in todo.py

# However, different team members can work on different stories in parallel:

Team Member A (User Story 1):
  - T006: Implement TodoManager.add_todo method
  - T007: Implement CLI handler for Add Todo
  - T008: Add error handling for empty description
  - T009: Integrate Add Todo handler

Team Member B (User Story 2):
  - T010: Implement TodoManager.list_todos method
  - T011: Implement CLI handler for View Todos
  - T012: Add "No todos found" message
  - T013: Format todo display
  - T014: Integrate View Todos handler

# Merge work after both complete their stories
```

---

## Implementation Strategy

### MVP First (User Stories 1-3 Only - All P1)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002-T005) - CRITICAL, blocks all stories
3. Complete Phase 3: User Story 1 - Create (T006-T009)
4. Complete Phase 5: User Story 3 - Complete (T015-T020)
   - Skip Phase 4 (View) initially - can test completion by inspecting state
5. **STOP and VALIDATE**: Test Create and Complete functionality independently
6. Add Phase 4 (View) for better user experience if time permits
7. Deploy/demo if ready

**MVP Minimum**: Setup + Foundational + US1 (Create) + US3 (Complete) = Users can add and complete todos

### Incremental Delivery (Recommended)

1. Complete Setup + Foundational (T001-T005) → Foundation ready
2. Add User Story 1 - Create (T006-T009) → Test independently → Deploy/Demo (Basic MVP)
3. Add User Story 2 - View (T010-T014) → Test independently → Deploy/Demo (Better UX)
4. Add User Story 3 - Complete (T015-T020) → Test independently → Deploy/Demo (Complete P1)
5. Add User Story 4 - Delete (T021-T026) → Test independently → Deploy/Demo (Full Feature Set)
6. Complete Polish phase (T027-T031)
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers (single-file constraint):

1. Team completes Setup + Foundational (T001-T005) together
2. Once Foundational is done:
   - Developer A: User Story 1 - Create (T006-T009)
   - Developer B: User Story 2 - View (T010-T014)
   - Developer C: User Story 3 - Complete (T015-T020)
3. Merge changes sequentially, resolving conflicts in single file
4. Developer A or B: User Story 4 - Delete (T021-T026)
5. Team: Polish phase (T027-T031)

**Note**: Single-file architecture means merge conflicts will occur frequently. Coordinate carefully or use feature branches with frequent merges.

---

## Notes

- **Single-file architecture**: All code in todo.py per Simplicity First principle
- **No automated tests**: Phase 1 uses manual CLI testing only
- **[P] marker**: Not used extensively due to single-file constraint - most tasks are sequential
- **[Story] label**: Maps task to specific user story for traceability (US1-US4)
- **No story label**: Setup, Foundational, and Polish phases
- **Each user story independently testable**: Create todos → View → Complete → Delete in any order
- **MVP**: User Stories 1-3 (Create, View, Complete) deliver core value
- **P2 story**: User Story 4 (Delete) is optional - users can ignore completed todos
- **Test after each story**: Verify functionality independently before proceeding
- **Match contract specs**: All prompts and error messages must match contracts/cli-interface.md
- **Quickstart validation**: Run quickstart.md scenarios as final acceptance test
