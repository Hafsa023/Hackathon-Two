---
id: 001
title: Create project constitution
stage: constitution
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: User
command: sp.constitution
labels: ["constitution","governance","project-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests: []
---

## Prompt

```text
# 📜 Project Constitution — CLI Todo Application

## 1. Project Overview
This project aims to build a **command-line Todo application** using **spec-driven development** powered by **Claude Code** and **Spec-Kit Plus**.
All development must strictly follow the **Agentic Dev Stack workflow** without any manual coding.

The application will manage tasks **in-memory** and demonstrate clean architecture, maintainability, and proper development iteration history.

---

## 2. Objective
Build a fully functional **CLI Todo Application** that allows users to:
- Add tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks as complete or incomplete

The system must store tasks **in memory only** (no database or file persistence).

---

## 3. Development Rules & Constraints
- ❌ **No manual coding is allowed**
- ✅ All code must be generated using **Claude Code**
- ✅ Specifications must be created and evolved using **Spec-Kit Plus**
- ✅ Each development phase must be traceable and reviewable
- ✅ Follow **clean code principles** and **Python best practices**

---

## 4. Development Workflow (Agentic Dev Stack)
The project must strictly follow this workflow:

1. **Write Specification**
   - Define functional and non-functional requirements using Spec-Kit Plus
2. **Generate Plan**
   - Convert specifications into a structured development plan
3. **Task Breakdown**
   - Decompose the plan into executable development tasks
4. **Implementation**
   - Use Claude Code to implement tasks iteratively
5. **Iteration & Refinement**
   - Update specs when changes occur and store history

---

## 5. Functional Requirements
The application must implement **all 5 Basic Level features**:

1. **Add Task**
   - Accept task title and description
   - Assign a unique ID
   - Default status: incomplete

2. **View Tasks**
   - List all tasks
   - Display ID, title, description, and completion status

3. **Update Task**
   - Modify title and/or description using task ID

4. **Delete Task**
   - Remove a task using its ID

5. **Mark Task Complete / Incomplete**
   - Toggle completion status by ID

---

## 6. Non-Functional Requirements
- Clear CLI output with readable formatting
- Maintainable and modular code
- Separation of concerns (logic, models, CLI handling)
- Consistent naming conventions
- Pythonic error handling

---

## 7. Technology Stack
- **Python:** 3.13+
- **Package Manager:** UV
- **Specification Tool:** Spec-Kit Plus
- **Code Generation:** Claude Code

---

## 8. Project Structure Requirements
The GitHub repository must include:
```

## Response snapshot

Created initial project constitution at `.specify/memory/constitution.md` with:
- 5 core principles (Spec-Driven Development, Agentic Code Generation, In-Memory Architecture, Clean Architecture, Traceable Development History)
- Technology stack section (Python 3.13+, UV, Spec-Kit Plus, Claude Code)
- Development workflow section (Agentic Dev Stack)
- Functional and non-functional requirements
- Project structure requirements
- Governance section with amendment process and versioning policy

## Outcome

- ✅ Impact: Project constitution established as authoritative source for development practices
- 🧪 Tests: None required for constitution creation
- 📁 Files: 1 created (.specify/memory/constitution.md)
- 🔁 Next prompts: Create feature specification with /sp.spec
- 🧠 Reflection: Constitution provides clear constraints for agentic development workflow

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment: N/A
