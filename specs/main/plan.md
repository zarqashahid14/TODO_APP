# Implementation Plan: Phase 1 Todo CLI App

**Branch**: `main` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/main/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Phase 1 delivers a minimal CLI-based todo application in Python 3.11. The app follows the Simplicity First principle with a TodoManager class handling CRUD operations and a main() function providing a continuous CLI menu loop. Storage is an in-memory list of dictionaries. All user input is protected with try-except blocks for error handling.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: None (standard library only - input(), print(), built-in types)
**Storage**: In-memory list of dictionaries (transient, lost on exit)
**Testing**: Manual CLI testing (no automated test framework for Phase 1)
**Target Platform**: Linux/Windows/macOS (any Python 3.11+ runtime)
**Project Type**: Single project (CLI script)
**Performance Goals**: None (interactive CLI - sub-second response times sufficient)
**Constraints**: No external dependencies, no database, no persistent storage (Phase 1 only)
**Scale/Scope**: Single-user, single-session, unlimited todo items (bounded only by available memory)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### I. Simplicity First (NON-NEGOTIABLE)

- [x] **Explicit over implicit**: TodoManager class methods are named clearly (add, list, complete, delete); CLI menu options are numbered 1-5
- [x] **Avoid premature optimization**: No caching, no indexes, no threading - simple list operations only
- [x] **Use existing tools**: Python standard library only (no external dependencies)
- [x] **Maximum 3 layers of abstraction**:
  1. User (CLI menu input)
  2. main() function (menu routing)
  3. TodoManager class (data operations)
- [x] **Explainability**: "Add todo with description, mark complete, view list, delete, exit" - explainable in 1 sentence

### II. Testable Features

- [x] **Independent test paths**: Each user story (Create, View, Complete, Delete) can be tested standalone
- [x] **Acceptance scenarios**: All scenarios written in Given/When/Then format in spec.md
- [x] **Edge cases enumerated**: Invalid IDs, empty input, special characters, whitespace handled in spec
- [x] **No implementation without test path**: spec.md defined before plan.md created

### III. MVP-First Delivery

- [x] **P1 stories independently deliverable**:
  - Story 1 (Create): Users can add todos - delivers value
  - Story 2 (View): Users can see their todos - delivers value
  - Story 3 (Complete): Users can mark done - delivers value
- [x] **P2 story (Delete) optional**: Users can work around by ignoring completed todos
- [x] **Each checkpoint produces working artifact**: After each user story, CLI has demonstrable functionality

### IV. Spec-Driven Development

- [x] **No code without spec.md**: spec.md created and populated with user stories
- [x] **No code without plan.md**: This plan.md created before implementation
- [x] **No code without tasks.md**: Will be created by /sp.tasks command next
- [x] **Artifacts versioned and linked**: plan.md links to spec.md

### Technology Stack Constraints

- [x] **Python 3.11**: Matches constitution constraint
- [x] **Storage**: Using in-memory list (pre-MVP, acceptable for Phase 1)
- [x] **No external deps**: Constitution constraint satisfied

### Quality Gates

- [x] **Simplicity principle**: 3-layer max, no over-engineering
- [x] **Testability**: All user stories have independent test paths
- [x] **MVP-first**: P1 stories deliver complete value

### Gate Status: ✅ PASS

---

## Post-Design Constitution Check

*Re-evaluated after Phase 1 design artifacts created*

### I. Simplicity First (NON-NEGOTIABLE) - Post-Design Review

- [x] **Data model**: Single Todo entity with 3 fields (id, description, status) - no over-engineering
- [x] **Storage**: In-memory list - matches Simplicity First decision in research.md
- [x] **API contracts**: CLI interface with 5 numbered options - no argparse complexity
- [x] **Error handling**: All user input wrapped in try-except - documented in contracts/cli-interface.md
- [x] **Code structure**: Single file (todo.py) - documented in Project Structure

**Post-Design Findings**: No violations. All design choices align with Simplicity First.

---

### II. Testable Features - Post-Design Review

- [x] **Data model defines clear entities**: Todo entity with validation rules in data-model.md
- [x] **CLI interface contract**: All 5 operations have explicit input/output contracts (contracts/cli-interface.md)
- [x] **Edge cases documented**: Error responses defined for all user paths (invalid choice, empty input, non-existent IDs)
- [x] **Test scenarios**: quickstart.md provides complete example session for manual testing

**Post-Design Findings**: All user stories have clear, testable contracts. No gaps identified.

---

### III. MVP-First Delivery - Post-Design Review

- [x] **P1 stories independently deliverable**:
  - Story 1 (Create): TodoManager.add_todo() + CLI option 1 - complete
  - Story 2 (View): TodoManager.list_todos() + CLI option 2 - complete
  - Story 3 (Complete): TodoManager.complete_todo() + CLI option 3 - complete
- [x] **P2 story (Delete) optional**: TodoManager.delete_todo() + CLI option 4 - complete
- [x] **No dependencies between stories**: Each operation is independent
- [x] **Quickstart validates MVP**: User can add, view, complete, delete in any order

**Post-Design Findings**: Each story can be implemented and tested independently. No blocking dependencies.

---

### IV. Spec-Driven Development - Post-Design Review

- [x] **spec.md complete**: User stories, acceptance criteria, edge cases, requirements defined
- [x] **plan.md complete**: Architecture, data model, contracts, research documented
- [x] **Artifacts versioned and linked**: All artifacts reference each other via Markdown links
- [x] **No implementation started**: No code written yet (waiting for tasks.md)

**Post-Design Findings**: Full spec-driven workflow followed. Ready for tasks generation.

---

### Technology Stack - Post-Design Review

- [x] **Python 3.11**: Confirmed in Technical Context
- [x] **No external dependencies**: Standard library only (data-model.md confirms dict/list usage)
- [x] **CLI interface**: No web frontend - single project type confirmed
- [x] **In-memory storage**: Transient, acceptable for Phase 1 (research.md rationale)

**Post-Design Findings**: Technology stack constraints satisfied. No drift from constitution.

---

### Post-Design Gate Status: ✅ PASS

**Summary**: All design artifacts (research.md, data-model.md, contracts/cli-interface.md, quickstart.md) satisfy constitution principles. No violations found. Ready for Phase 2 (tasks.md generation via `/sp.tasks`).

## Project Structure

### Documentation (this feature)

```text
specs/main/
├── spec.md              # Feature specification (/sp.specify command)
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
.
├── todo.py              # Main CLI application (TodoManager class + main())
├── specs/               # Specification and planning artifacts
└── history/             # PHRs and ADRs
```

**Structure Decision**: Single-file Python script (todo.py) following Simplicity First. The TodoManager class and main() function coexist in one file. No separate src/ directory needed for a single CLI script. No tests/ directory for Phase 1 (manual CLI testing only).

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
