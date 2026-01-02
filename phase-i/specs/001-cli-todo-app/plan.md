# Development Plan: CLI Todo Application

**Branch**: `001-cli-todo-app`
**Date**: 2025-12-31
**Spec**: [spec.md](spec.md)

## Summary

This plan outlines the development approach for a CLI Todo Application that provides task management capabilities through a command-line interface. The application will store tasks in-memory and implement clean architecture with clear separation between models, services, and CLI handling.

The development follows a phased approach starting with infrastructure setup, then building the data layer, service layer, and finally the CLI interface. Each phase includes validation checkpoints to ensure quality before proceeding.

---

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: argparse (stdlib), sys (stdlib)
**Storage**: In-memory list/dictionary (no persistence)
**Testing**: pytest (standard Python testing)
**Target Platform**: Cross-platform (Linux, macOS, Windows)
**Project Type**: Single CLI application
**Performance Goals**: All commands complete within 100ms (NFR-001)
**Constraints**: No external libraries, clean architecture, no persistence
**Scale/Scope**: Single user, up to 1,000 tasks (NFR-006)

---

## Constitution Check

The following gates verify compliance with the project constitution:

| Principle | Compliance Requirement | Status |
|-----------|----------------------|--------|
| I. Spec-Driven Development | All code follows spec, no implementation before planning | ✅ |
| II. Agentic Code Generation | All code generated via Claude Code, no manual coding | ✅ |
| III. In-Memory Architecture | No file/database persistence, session-only storage | ✅ |
| IV. Clean Architecture | Models, services, CLI layers clearly separated | ✅ |
| V. Traceable History | All phases documented in specs/ and history/prompts/ | ✅ |

**Gate Status**: ✅ PASSED - Proceed with development planning

---

## Project Structure

### Source Code

```
src/
├── models/
│   └── task.py          # Task entity class
├── services/
│   └── task_service.py  # Business logic for task operations
├── cli/
│   ├── __init__.py
│   ├── parser.py        # Argument parsing setup
│   └── commands.py      # CLI command handlers
└── __init__.py

tests/
├── unit/
│   ├── test_task.py
│   └── test_task_service.py
└── integration/
    └── test_cli.py
```

### Documentation Structure

```
specs/001-cli-todo-app/
├── spec.md              # Feature specification
├── plan.md              # This file
└── checklists/
    └── requirements.md  # Quality checklist
```

---

## Development Phases

### Phase 1: Project Foundation

**Goal**: Initialize project structure and dependencies

**Key Activities**:
- Set up project directory structure
- Configure pyproject.toml for Python 3.13+
- Set up pytest for testing
- Create initial `__init__.py` files
- Configure linting/formatting (if needed)

**Requirements Addressed**:
- NFR-004: Clean architecture with separated layers
- NFR-005: Python best practices

**Deliverables**:
- `src/` directory with proper package structure
- `tests/` directory with test framework configured
- `pyproject.toml` with project metadata

**Validation Checkpoint**:
- [ ] Project structure matches plan
- [ ] Tests can be discovered and run
- [ ] Python import paths work correctly

---

### Phase 2: Data Layer - Task Model

**Goal**: Define the Task entity with all required attributes

**Key Activities**:
- Create `src/models/task.py`
- Implement Task class with:
  - `id`: int (unique identifier)
  - `title`: str (1-100 chars)
  - `description`: str (optional)
  - `status`: str ("incomplete" or "complete")
- Add validation for title length (1-100 chars)
- Add `__repr__` for debugging
- Add equality comparison based on ID

**Requirements Addressed**:
- FR-002: Unique auto-incrementing ID
- FR-003: Default status to "incomplete"
- NFR-004: Clean architecture (models layer)

**Deliverables**:
- `src/models/task.py`: Task class with validation
- `tests/unit/test_task.py`: Unit tests for Task model

**Validation Checkpoint**:
- [ ] Task can be created with all required fields
- [ ] Title validation works (1-100 chars)
- [ ] Default status is "incomplete"
- [ ] ID-based equality works correctly

---

### Phase 3: Service Layer - Task Management

**Goal**: Implement business logic for all task operations

**Key Activities**:
- Create `src/services/task_service.py`
- Implement TaskService class with:
  - In-memory task storage (dict for O(1) lookups by ID)
  - Auto-incrementing ID counter
  - CRUD operations:
    - `add_task(title, description)` -> Task
    - `get_all_tasks()` -> List[Task]
    - `get_task_by_id(id)` -> Task | None
    - `update_task(id, title, description)` -> Task | None
    - `delete_task(id)` -> bool
    - `mark_complete(id)` -> Task | None
    - `mark_incomplete(id)` -> Task | None
- Add error handling for not found IDs
- Ensure idempotent operations (complete on already-complete task)

**Requirements Addressed**:
- FR-001: Add tasks with title and description
- FR-002: Unique auto-incrementing ID
- FR-003: Default incomplete status
- FR-004: View all tasks
- FR-005: Update tasks by ID
- FR-006: Delete tasks by ID
- FR-007: Mark complete by ID
- FR-008: Mark incomplete by ID
- FR-011: Store tasks in memory
- FR-012: Maintain task IDs unchanged
- NFR-001: Operations complete within 100ms
- NFR-006: Handle 1,000+ tasks

**Deliverables**:
- `src/services/task_service.py`: TaskService class
- `tests/unit/test_task_service.py`: Service unit tests

**Validation Checkpoint**:
- [ ] All CRUD operations work correctly
- [ ] ID auto-increment works (1, 2, 3...)
- [ ] Update preserves unmodified fields
- [ ] Delete removes task from storage
- [ ] Mark complete/incomplete toggles status
- [ ] Operations are idempotent
- [ ] Error handling for invalid IDs

---

### Phase 4: CLI Interface Layer

**Goal**: Build command-line interface with all required commands

**Key Activities**:
- Create `src/cli/parser.py`:
  - Set up argparse.ArgumentParser
  - Configure subcommands: add, list, update, delete, complete, incomplete
  - Add help flags for each command

- Create `src/cli/commands.py`:
  - Implement `add` command handler
  - Implement `list` command formatter
  - Implement `update` command handler
  - Implement `delete` command handler
  - Implement `complete` command handler
  - Implement `incomplete` command handler
  - Implement error output to stderr
  - Implement exit codes per error type

- Create `src/cli/__init__.py`:
  - Expose main entry point function

**Requirements Addressed**:
- FR-009: Display appropriate error messages
- FR-010: Provide help information
- NFR-002: Human-readable output format
- NFR-003: Clear, actionable error messages

**Deliverables**:
- `src/cli/parser.py`: Argument parsing configuration
- `src/cli/commands.py`: Command handlers
- `src/cli/__init__.py`: Package exports
- `src/__main__.py`: Entry point for `python -m todo`

**Validation Checkpoint**:
- [ ] All 6 commands parse correctly
- [ ] Help displays for `--help` flag
- [ ] Error messages match spec
- [ ] Exit codes are correct (1 for errors)
- [ ] Output formatting is readable

---

### Phase 5: Integration & Main Entry Point

**Goal**: Connect CLI layer to service layer and create executable entry point

**Key Activities**:
- Create `src/__main__.py`:
  - Parse arguments
  - Instantiate TaskService
  - Route to appropriate command handler
  - Handle exceptions and display errors
  - Return appropriate exit codes

- Create `pyproject.toml` entry points:
  - `console_scripts` for `todo` command

- Verify all error types output to stderr

**Requirements Addressed**:
- All FRs (integration point)
- NFR-001: 100ms command completion
- NFR-002: Human-readable output
- NFR-003: Clear error messages

**Deliverables**:
- `src/__main__.py`: Main entry point
- `pyproject.toml`: Console script entry point

**Validation Checkpoint**:
- [ ] `todo --help` works
- [ ] `todo add "title" "desc"` creates task
- [ ] `todo list` displays tasks
- [ ] `todo update 1 --title "new"` updates
- [ ] `todo delete 1` removes task
- [ ] `todo complete 1` marks complete
- [ ] `todo incomplete 1` marks incomplete
- [ ] Error messages appear on stderr
- [ ] Exit codes are correct

---

### Phase 6: Testing & Validation

**Goal**: Comprehensive testing of all functionality

**Key Activities**:
- Write unit tests for Task model
- Write unit tests for TaskService
- Write integration tests for CLI
- Verify all acceptance scenarios pass
- Performance testing (100ms requirement)
- Large dataset testing (1,000 tasks)

**Requirements Addressed**:
- All FRs (via test verification)
- NFR-001: Performance requirement
- NFR-006: Scale requirement

**Deliverables**:
- `tests/unit/test_task.py`: Task model tests
- `tests/unit/test_task_service.py`: Service tests
- `tests/integration/test_cli.py`: CLI integration tests
- Test coverage report

**Validation Checkpoint**:
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] All acceptance scenarios verified
- [ ] Performance < 100ms per command
- [ ] 1,000 tasks load and display correctly

---

## Phase Dependencies

```
Phase 1 (Foundation)
    │
    ▼
Phase 2 (Task Model) ──────┐
    │                      │
    ▼                      │
Phase 3 (Task Service)     │
    │                      │
    └──────┬───────────────┘
           │
           ▼
Phase 4 (CLI Interface)
           │
           ▼
Phase 5 (Integration)
           │
           ▼
Phase 6 (Testing)
```

---

## Requirements Traceability

### Functional Requirements Mapping

| Requirement | Phase | Component | File |
|-------------|-------|-----------|------|
| FR-001: Add tasks | Phase 3 | Service | `task_service.py` |
| FR-002: Unique IDs | Phase 3 | Service | `task_service.py` |
| FR-003: Default incomplete | Phase 2 | Model | `task.py` |
| FR-004: View tasks | Phase 3 | Service | `task_service.py` |
| FR-005: Update tasks | Phase 3 | Service | `task_service.py` |
| FR-006: Delete tasks | Phase 3 | Service | `task_service.py` |
| FR-007: Mark complete | Phase 3 | Service | `task_service.py` |
| FR-008: Mark incomplete | Phase 3 | Service | `task_service.py` |
| FR-009: Error messages | Phase 4 | CLI | `commands.py`, `parser.py` |
| FR-010: Help info | Phase 4 | CLI | `parser.py` |
| FR-011: In-memory storage | Phase 3 | Service | `task_service.py` |
| FR-012: Stable IDs | Phase 3 | Service | `task_service.py` |

### Non-Functional Requirements Mapping

| Requirement | Phase | Component | Verification |
|-------------|-------|-----------|--------------|
| NFR-001: <100ms | Phase 6 | All | Performance testing |
| NFR-002: Readable output | Phase 4 | CLI | Output review |
| NFR-003: Clear errors | Phase 4 | CLI | Error message review |
| NFR-004: Clean architecture | All | Structure | Structure review |
| NFR-005: Python best practices | All | All | Linting/Code review |
| NFR-006: 1,000 tasks | Phase 6 | Service | Scale testing |

---

## Success Criteria Validation

| Criterion | Phase | Verification Method |
|-----------|-------|---------------------|
| SC-001: Add task appears in list | Phase 6 | Integration test |
| SC-002: List shows all tasks | Phase 6 | Integration test |
| SC-003: Update changes task | Phase 6 | Integration test |
| SC-004: Delete removes task | Phase 6 | Integration test |
| SC-005: Toggle completion | Phase 6 | Integration test |
| SC-006: Clear output/errors | Phase 6 | Output review |
| SC-007: IDs stable/unique | Phase 6 | Unit tests |

---

## Architecture Decision Records

No ADRs required for this feature. All architectural decisions follow standard patterns:
- Single project structure for CLI application
- In-memory storage using Python dict
- argparse for CLI parsing (stdlib)
- pytest for testing (standard Python testing)

---

## Complexity Tracking

No constitution violations detected. All decisions follow the simplest viable approach:
- Single project structure (no unnecessary complexity)
- In-memory storage (matches requirements)
- argparse stdlib (no external dependencies)
- Sequential phases (clear dependency order)

---

## Notes

- All code must be generated using Claude Code (Constitution II)
- No manual coding permitted at any phase
- Each phase must pass validation checkpoint before proceeding
- PHR records must be created for each phase completion
- Spec updates required if any requirements change
