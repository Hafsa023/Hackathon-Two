---
description: "Task list for CLI Todo Application implementation"
---

# Tasks: CLI Todo Application

**Input**: Design documents from `/specs/001-cli-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)
**Tests**: Unit tests and integration tests included

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow the project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure per implementation plan in src/models/, src/services/, src/cli/, tests/unit/, tests/integration/
- [X] T002 Create pyproject.toml with Python 3.13+, project metadata, pytest configuration, and console_scripts entry point
- [X] T003 [P] Create __init__.py files in src/, src/models/, src/services/, src/cli/, tests/, tests/unit/, tests/integration/
- [X] T004 [P] Create pytest.ini or configure pytest in pyproject.toml for test discovery

**Checkpoint**: Project structure matches plan, tests can be discovered

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Create Task model class in src/models/task.py with id, title, description, status attributes
- [X] T006 [P] Add Task.__init__ method with title validation (1-100 chars), default status="incomplete"
- [X] T007 [P] Add Task.__repr__ method for debugging in src/models/task.py
- [X] T008 [P] Add Task.__eq__ method based on task ID in src/models/task.py
- [X] T009 [P] Add Task.to_dict method for serialization in src/models/task.py
- [X] T010 Create unit tests for Task model in tests/unit/test_task.py covering initialization, validation, and equality

**Checkpoint**: Task model complete - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks with a title and optional description

**Independent Test**: Run `todo add "Test task" "desc"` and verify task appears in `todo list` output with unique ID and "incomplete" status

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T011 [P] [US1] Unit test for add_task method in tests/unit/test_task_service.py (test_id_auto_increment, test_title_validation, test_description_optional)
- [X] T012 [P] [US1] Integration test for add CLI command in tests/integration/test_cli.py (test_add_creates_task, test_add_with_description, test_add_empty_title_error, test_add_title_too_long_error)

### Implementation for User Story 1

- [X] T013 [US1] Create TaskService class with in-memory task storage (dict) and auto-incrementing ID counter in src/services/task_service.py
- [X] T014 [US1] Implement add_task method in src/services/task_service.py with title validation (1-100 chars) and optional description
- [X] T015 [US1] Create argparse subcommand configuration for add command in src/cli/parser.py
- [X] T016 [US1] Implement add command handler in src/cli/commands.py that calls TaskService.add_task
- [X] T017 [US1] Add error handling for empty title and title too long in src/cli/commands.py

**Checkpoint**: User Story 1 functional - `todo add "title"` creates task with ID and "incomplete" status

---

## Phase 4: User Story 2 - View Tasks (Priority: P1)

**Goal**: Users can view all tasks in a formatted display

**Independent Test**: Run `todo list` after adding tasks and verify output shows all tasks with ID, Title, Description, Status columns

### Tests for User Story 2

- [ ] T018 [P] [US2] Unit test for get_all_tasks method in tests/unit/test_task_service.py (test_get_all_tasks_returns_list, test_get_all_tasks_empty)
- [ ] T019 [P] [US2] Integration test for list CLI command in tests/integration/test_cli.py (test_list_empty_message, test_list_displays_tasks, test_list_shows_status)

### Implementation for User Story 2

- [ ] T020 [US2] Implement get_all_tasks method in src/services/task_service.py returning list of Task objects
- [ ] T021 [US2] Create task formatter in src/cli/commands.py for displaying tasks in readable table format
- [ ] T022 [US2] Implement list command handler in src/cli/commands.py that calls TaskService.get_all_tasks and formats output
- [ ] T023 [US2] Add empty list message handling in src/cli/commands.py

**Checkpoint**: User Story 2 functional - `todo list` shows all tasks with proper formatting

---

## Phase 5: User Story 3 - Update Tasks (Priority: P1)

**Goal**: Users can update task title and/or description by ID

**Independent Test**: Run `todo update 1 --title "New title"` and verify change appears in `todo list`

### Tests for User Story 3

- [ ] T024 [P] [US3] Unit test for update_task method in tests/unit/test_task_service.py (test_update_title, test_update_description, test_update_both, test_update_preserves_unmodified, test_update_not_found)
- [ ] T025 [P] [US3] Integration test for update CLI command in tests/integration/test_cli.py (test_update_title, test_update_description, test_update_not_found_error)

### Implementation for User Story 3

- [ ] T026 [US3] Implement update_task method in src/services/task_service.py allowing title and/or description updates by ID
- [ ] T027 [US3] Create argparse arguments for update command (--title, --description) in src/cli/parser.py
- [ ] T028 [US3] Implement update command handler in src/cli/commands.py that calls TaskService.update_task
- [ ] T029 [US3] Add task not found error handling in src/cli/commands.py

**Checkpoint**: User Story 3 functional - `todo update 1 --title "new"` updates task successfully

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P1)

**Goal**: Users can delete tasks by ID

**Independent Test**: Run `todo delete 1` and verify task no longer appears in `todo list`

### Tests for User Story 4

- [ ] T030 [P] [US4] Unit test for delete_task method in tests/unit/test_task_service.py (test_delete_removes_task, test_delete_not_found)
- [ ] T031 [P] [US4] Integration test for delete CLI command in tests/integration/test_cli.py (test_delete_removes_task, test_delete_not_found_error)

### Implementation for User Story 4

- [ ] T032 [US4] Implement delete_task method in src/services/task_service.py returning bool for success/failure
- [ ] T033 [US4] Create argparse argument for delete command (positional id) in src/cli/parser.py
- [ ] T034 [US4] Implement delete command handler in src/cli/commands.py that calls TaskService.delete_task
- [ ] T035 [US4] Add task not found error handling for delete in src/cli/commands.py

**Checkpoint**: User Story 4 functional - `todo delete 1` removes task successfully

---

## Phase 7: User Story 5 - Mark Complete/Incomplete (Priority: P1)

**Goal**: Users can toggle task completion status by ID

**Independent Test**: Run `todo complete 1` then `todo list` verify status "complete", then `todo incomplete 1` verify status "incomplete"

### Tests for User Story 5

- [ ] T036 [P] [US5] Unit test for mark_complete and mark_incomplete methods in tests/unit/test_task_service.py (test_mark_complete, test_mark_incomplete, test_mark_complete_idempotent, test_mark_not_found)
- [ ] T037 [P] [US5] Integration test for complete/incomplete CLI commands in tests/integration/test_cli.py (test_complete_changes_status, test_incomplete_changes_status, test_complete_not_found_error)

### Implementation for User Story 5

- [ ] T038 [US5] Implement mark_complete method in src/services/task_service.py (idempotent operation)
- [ ] T039 [US5] Implement mark_incomplete method in src/services/task_service.py
- [ ] T040 [US5] Create argparse arguments for complete command (positional id) in src/cli/parser.py
- [ ] T041 [US5] Create argparse arguments for incomplete command (positional id) in src/cli/parser.py
- [ ] T042 [US5] Implement complete command handler in src/cli/commands.py that calls TaskService.mark_complete
- [ ] T043 [US5] Implement incomplete command handler in src/cli/commands.py that calls TaskService.mark_incomplete
- [ ] T044 [US5] Add task not found error handling for complete/incomplete in src/cli/commands.py

**Checkpoint**: User Story 5 functional - `todo complete 1` and `todo incomplete 1` toggle status correctly

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Integration, performance, and final validation

- [X] T045 Create main entry point in src/__main__.py that parses arguments, instantiates TaskService, and routes to command handlers
- [X] T046 [P] Verify pyproject.toml console_scripts entry point configured correctly for `todo` command
- [X] T047 [P] Write comprehensive integration test covering full user workflow in tests/integration/test_cli.py (test_full_workflow_add_list_update_complete)
- [X] T048 [P] Run all unit tests and verify 100% pass rate
- [X] T049 [P] Run all integration tests and verify all scenarios pass
- [X] T050 [P] Performance test: verify all commands complete within 100ms with 1000 tasks
- [X] T051 [P] Verify all error messages match specification and output to stderr with exit code 1
- [X] T052 [P] Verify help command works: `todo --help` and `todo <command> --help`

**Checkpoint**: All phases complete - application ready for demo

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup) ──────────┐
                          │
Phase 2 (Foundational) ───┤
                          │
Phase 3 (US1: Add) ───────┤── All user stories can proceed in parallel after Phase 2
Phase 4 (US2: View) ──────┤
Phase 5 (US3: Update) ────┤
Phase 6 (US4: Delete) ────┤
Phase 7 (US5: Toggle) ────┘
                          │
Phase 8 (Polish) ─────────┘ (depends on all user stories complete)
```

### User Story Dependencies

- **User Story 1 (Add)**: Can start after Phase 2 - No dependencies on other stories
- **User Story 2 (View)**: Can start after Phase 2 - No dependencies on other stories
- **User Story 3 (Update)**: Can start after Phase 2 - No dependencies on other stories
- **User Story 4 (Delete)**: Can start after Phase 2 - No dependencies on other stories
- **User Story 5 (Toggle)**: Can start after Phase 2 - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Service methods before CLI handlers
- Core implementation before error handling
- Story complete before moving to next priority

### Parallel Opportunities

- All Phase 1 tasks marked [P] can run in parallel
- All Phase 2 tasks marked [P] can run in parallel
- Once Phase 2 completes, all user stories (Phases 3-7) can proceed in parallel
- All test tasks within a story marked [P] can run in parallel
- Phase 8 polish tasks marked [P] can run in parallel

---

## Parallel Execution Examples

```bash
# Parallel execution after Phase 2:
# Developer A: User Story 1 (Add Tasks) - T011, T012, T013-T017
# Developer B: User Story 2 (View Tasks) - T018, T019, T020-T023
# Developer C: User Story 3 (Update Tasks) - T024, T025, T026-T029

# All Phase 8 tasks can run in parallel after all stories complete:
# T045, T046, T047, T048, T049, T050, T051, T052
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (blocks all stories)
3. Complete Phase 3: User Story 1 (Add Tasks)
4. **STOP and VALIDATE**: Test add command independently
5. Demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently
3. Add User Story 2 → Test independently
4. Add User Story 3 → Test independently
5. Add User Story 4 → Test independently
6. Add User Story 5 → Test independently
7. Polish phase → Complete application

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Add)
   - Developer B: User Story 2 (View)
   - Developer C: User Story 3 (Update)
   - Developer D: User Stories 4-5 (Delete/Toggle)
3. Stories complete and integrate in Phase 8

---

## Task Summary

| Phase | Task Count | Description |
|-------|------------|-------------|
| Phase 1: Setup | 4 | Project structure, pyproject.toml, __init__.py files |
| Phase 2: Foundational | 6 | Task model with validation |
| Phase 3: US1 Add | 7 | Add task service + CLI command |
| Phase 4: US2 View | 6 | List tasks service + formatter |
| Phase 5: US3 Update | 6 | Update task service + CLI command |
| Phase 6: US4 Delete | 5 | Delete task service + CLI command |
| Phase 7: US5 Toggle | 8 | Complete/incomplete service + CLI commands |
| Phase 8: Polish | 8 | Integration, testing, performance |
| **Total** | **50** | All implementation tasks |

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
