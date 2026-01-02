<!--
Sync Impact Report:
  Version change: N/A → 1.0.0 (initial creation)
  Added sections:
    - Core Principles (5 principles derived from user requirements)
    - Technology Stack section
    - Development Workflow section
    - Project Structure Requirements section
  Removed sections: None (template sections replaced with project-specific content)
  Templates requiring updates: ✅ All templates already compatible with constitution structure
-->

# CLI Todo Application Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)

All development MUST follow the Spec-Kit Plus workflow. Every feature begins with a written
specification before any code is written. Specifications MUST be created using the `/sp.spec`
command and stored in `specs/<feature>/spec.md`. No implementation code may be written until
the specification is complete and approved.

**Rationale**: Ensures clear requirements, traceability, and prevents scope creep.

### II. Agentic Code Generation (NON-NEGOTIABLE)

All code MUST be generated using Claude Code. No manual coding is permitted. The agent MUST use
MCP tools and CLI commands for all information gathering and task execution. The agent MUST
prefer MCP tools over internal knowledge.

**Rationale**: Ensures consistency, traceability, and adherence to the Agentic Dev Stack workflow.

### III. In-Memory Architecture

The application MUST store all tasks in memory only. No database or file persistence is allowed
for task storage. This constraint MUST be respected in all implementation decisions.

**Rationale**: Simplicity requirement for demonstration purposes; no persistence layer complexity.

### IV. Clean Architecture & Separation of Concerns

The codebase MUST maintain clear separation between:
- Models (data structures)
- Services (business logic)
- CLI handling (user interface)

Code MUST follow Python best practices, use consistent naming conventions, and include proper
error handling.

**Rationale**: Ensures maintainability and extensibility of the codebase.

### V. Traceable Development History

All development phases MUST be traceable and reviewable. This includes:
- Specifications in `specs/<feature>/`
- Plans in `specs/<feature>/plan.md`
- Tasks in `specs/<feature>/tasks.md`
- Prompt History Records in `history/prompts/`

**Rationale**: Enables code review, audit trails, and iterative improvement.

## Technology Stack

- **Language**: Python 3.13+
- **Package Manager**: UV
- **Specification Tool**: Spec-Kit Plus
- **Code Generation**: Claude Code
- **Storage**: In-memory (no database or file persistence)

## Development Workflow

The project MUST strictly follow the Agentic Dev Stack workflow:

1. **Write Specification** - Define functional and non-functional requirements using Spec-Kit Plus
2. **Generate Plan** - Convert specifications into a structured development plan
3. **Task Breakdown** - Decompose the plan into executable development tasks
4. **Implementation** - Use Claude Code to implement tasks iteratively
5. **Iteration & Refinement** - Update specs when changes occur and store history

## Functional Requirements

The application MUST implement these five basic features:

1. **Add Task** - Accept task title and description, assign unique ID, default status: incomplete
2. **View Tasks** - List all tasks with ID, title, description, and completion status
3. **Update Task** - Modify title and/or description using task ID
4. **Delete Task** - Remove a task using its ID
5. **Mark Complete/Incomplete** - Toggle completion status by ID

## Non-Functional Requirements

- Clear CLI output with readable formatting
- Maintainable and modular code structure
- Consistent naming conventions throughout
- Pythonic error handling with meaningful error messages

## Project Structure Requirements

The repository MUST include:
- `src/` - Source code directory
- `tests/` - Test files directory
- `specs/<feature>/` - Feature specifications
- `.specify/memory/constitution.md` - This constitution
- `history/prompts/` - Prompt History Records

## Governance

This constitution is the authoritative source for all project development practices. It
supersedes any conflicting guidance or conventions.

**Amendment Process**: Amendments to this constitution require:
1. Documentation of the proposed change
2. Review and approval by the project owner
3. Version increment following semantic versioning rules

**Versioning Policy**:
- MAJOR: Backward incompatible governance changes or principle removals
- MINOR: New principles added or materially expanded guidance
- PATCH: Clarifications, wording improvements, typo fixes

**Compliance**: All PRs and code reviews MUST verify adherence to constitution principles.
Complexity that cannot comply MUST be documented with justification in the plan document.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
