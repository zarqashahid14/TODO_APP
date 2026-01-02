# Research: Phase 1 Todo CLI App

**Feature**: Phase 1 - Todo CLI App
**Date**: 2026-01-01
**Purpose**: Document technical decisions and rationale for Phase 1 architecture

## Research Topics

### 1. In-Memory Storage (List of Dictionaries)

**Decision**: Use Python list of dictionaries for todo storage

**Rationale**:
- **Simplicity First**: No external dependencies, no database setup, no file I/O
- **MVP-focused**: Phase 1 is a prototype to validate the CLI interface and user flow
- **Fast iteration**: Allows immediate testing without persistence overhead
- **Hackathon-appropriate**: Matches time constraints for initial delivery

**Alternatives Considered**:
- **SQLite**: Provides persistence but adds complexity (DB setup, schema, migrations). Overkill for Phase 1.
- **JSON file storage**: Adds file I/O complexity, error handling for file operations, and potential race conditions. Defers to Phase 2+ if persistence needed.
- **Database (PostgreSQL)**: Violates Simplicity First for Phase 1. External service dependency not justified.

**Trade-offs**:
- ❌ Data lost on app exit (acceptable for Phase 1 prototype)
- ❌ No persistence between sessions (acceptable for hackathon demo)
- ✅ Zero external dependencies
- ✅ Instant setup (no DB configuration)
- ✅ Fast development pace

**Decision**: Proceed with in-memory list for Phase 1. Document persistence as Phase 2+ enhancement.

---

### 2. Single File vs. Multiple Files

**Decision**: Single Python file (todo.py) containing TodoManager class and main() function

**Rationale**:
- **Simplicity First**: All code visible in one place, no import complexity
- **MVP-sized**: Estimated <200 lines of code (fits comfortably in one file)
- **Fast execution**: No need to manage module imports or __init__.py files
- **Hackathon timeline**: Single file reduces cognitive load and debugging time

**Alternatives Considered**:
- **src/models/todo.py + src/cli/main.py**: Follows traditional Python project structure but adds unnecessary complexity for Phase 1. No clear benefit for a single CLI script.
- **Package with __init__.py**: Adds installation steps and import complexity. Overkill for a run-from-file script.

**Trade-offs**:
- ❌ Not scalable to larger applications (but Phase 1 is explicitly small)
- ❌ Less testable in isolation (but manual testing only for Phase 1)
- ✅ Instant understanding (read top-to-bottom in one file)
- ✅ No module search path issues
- ✅ Simpler deployment (just copy one file)

**Decision**: Single file for Phase 1. Refactor to package structure if Phase 2+ grows beyond 300 lines.

---

### 3. CLI Menu vs. Command-Line Arguments

**Decision**: Interactive CLI menu with numbered options (1-5) displayed in loop

**Rationale**:
- **User-friendly**: Clear options displayed, no need to memorize commands
- **Simplicity**: Simple while loop with input() for each operation
- **No argument parsing**: Avoids argparse complexity and help text generation
- **Guided workflow**: Forces users through available operations (good for hackathon demo)

**Alternatives Considered**:
- **argparse with subcommands** (e.g., `todo.py add "Buy groceries"`): More traditional CLI but requires help text, argument validation, and command dispatching. Adds ~50 lines of boilerplate.
- **Click/Typer libraries**: External dependencies violate Simplicity First. Overkill for 5 simple operations.

**Trade-offs**:
- ❌ Not scriptable/automatable (acceptable for Phase 1 demo)
- ❌ Slower for power users (not a target for Phase 1)
- ✅ Zero external dependencies
- ✅ No argument parsing logic
- ✅ Clear UI for non-technical users

**Decision**: Interactive menu for Phase 1. Consider CLI arguments if automation becomes a Phase 2+ requirement.

---

### 4. Error Handling Strategy

**Decision**: Try-except blocks wrapped around all user input operations

**Rationale**:
- **Constitution compliance**: Explicit error handling required for user input
- **Graceful degradation**: App continues running after invalid input
- **Clear error messages**: Users know what went wrong and what to do
- **Simple implementation**: Try-except is Pythonic and well-understood

**Alternatives Considered**:
- **Input validation before operations**: Validate input type and range first, then execute. More code than try-except.
- **Custom exception classes**: Adds boilerplate and indirection. Overkill for 5 operations.
- **Fail-fast (no error handling)**: Violates spec requirements (FR-009).

**Implementation Pattern**:
```python
try:
    user_input = int(input("Enter option: "))
except ValueError:
    print("Please enter a valid number.")
    continue
```

**Trade-offs**:
- ✅ Clear error messages
- ✅ App continues running
- ✅ Simple implementation
- ✅ Covers all user input paths

**Decision**: Try-except on all input() calls. Validate numeric input, list index ranges, and empty strings.

---

### 5. Todo ID Management

**Decision**: Incrementing integer IDs starting at 1, stable across deletions

**Rationale**:
- **User-friendly**: Humans understand "Todo #1", "Todo #3" better than UUIDs
- **Simple implementation**: Counter variable + 1 for each new todo
- **Stable IDs**: Don't reuse IDs after deletion (prevents confusion)
- **Matches CLI menu**: Users select by number anyway

**Alternatives Considered**:
- **UUIDs**: Universally unique but unfriendly for CLI (user must type full UUID). Overkill.
- **Hash of description**: Creates non-obvious IDs, same value for duplicates. Confusing.
- **Reusing gaps**: After deleting ID 2, next new todo becomes ID 2. Confusing if user expects IDs to be chronological.

**Implementation**:
```python
self.next_id = 1
def add_todo(self, description):
    todo = {
        'id': self.next_id,
        'description': description,
        'status': 'pending'
    }
    self.next_id += 1
    return todo
```

**Trade-offs**:
- ✅ Simple to implement
- ✅ User-friendly
- ✅ No ID collisions
- ❌ IDs can become large after many operations (acceptable for Phase 1)

**Decision**: Incrementing integer IDs for Phase 1. Monitor ID growth in Phase 2+.

---

## Phase 2+ Considerations

**Not in scope for Phase 1, but documented for future phases**:

1. **Persistence**: Consider SQLite or JSON file storage if data needs to survive app restarts
2. **Package structure**: Refactor to src/ layout if file exceeds 300 lines
3. **CLI arguments**: Add argparse support if automation/scriptability becomes a requirement
4. **Automated testing**: Add pytest and unit tests if Phase 2 adds complex logic
5. **ID recycling**: Consider reusing deleted IDs if maximum ID becomes an issue
6. **Todo features**: Tags, due dates, priorities (require spec updates)

---

## Conclusion

All research decisions align with the **Simplicity First** principle from the constitution. Phase 1 uses the absolute minimum complexity to deliver a working CLI todo app. Each decision deliberately avoids over-engineering in favor of fast delivery and clarity.

**Constitution Compliance**: ✅ All choices satisfy Simplicity First, MVP-First, and Testable Features principles.
