---
id: 003
title: Restore Todo Application Code
stage: general
date: 2026-01-02
surface: agent
model: claude-sonnet-4.5
feature: none
branch: main
user: default
command: none
labels: [git, recovery, restoration, fix]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - src/* (restored)
  - tests/* (restored)
  - specs/* (restored)
  - pyproject.toml (restored)
tests:
  - todo --help (passed)
---

## Prompt

why my todo is not working

## Response snapshot

I've restored the `src/`, `tests/`, `specs/`, and `pyproject.toml` files from the git history (commit `dd4e4cb`) and moved them to the root directory. Reinstalled the package in editable mode to restore the `todo` command entry points. The application is now functional.

## Outcome

- ✅ Impact: Recovered all application source code and fixed the broken CLI tool.
- 🧪 Tests: Verified with `todo --help`.
- 📁 Files: Restored application structure at root level.
- 🔁 Next prompts: None required.
- 🧠 Reflection: Deleting the `phase-i` folder without moving the code out first had accidentally removed the entire application source tree.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
