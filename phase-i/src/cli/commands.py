"""Command handlers for the todo CLI application."""

import argparse
import sys

from src.services.task_service import TaskService, TaskNotFoundError


def handle_add(args: argparse.Namespace, service: TaskService) -> int:
    """Handle the add command.

    Args:
        args: Parsed arguments containing title and description.
        service: TaskService instance.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    title = args.title
    description = getattr(args, "description", "") or ""

    try:
        service.add_task(title, description)
        print(f"Task added successfully (ID: {service.get_all_tasks()[-1].id})")
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def handle_list(args: argparse.Namespace, service: TaskService) -> int:
    """Handle the list command.

    Args:
        args: Parsed arguments (unused for list).
        service: TaskService instance.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    tasks = service.get_all_tasks()

    if not tasks:
        print("No tasks found. Add a task with 'todo add <title>'")
        return 0

    # Print header
    print(f"{'ID':<5} {'Status':<12} {'Title':<30} {'Description'}")
    print("-" * 80)

    # Print each task
    for task in tasks:
        status = "complete" if task.status == "complete" else "incomplete"
        title = task.title[:28] + ".." if len(task.title) > 30 else task.title
        desc = task.description[:40] if task.description else ""
        print(f"{task.id:<5} {status:<12} {title:<30} {desc}")

    return 0


def handle_update(args: argparse.Namespace, service: TaskService) -> int:
    """Handle the update command.

    Args:
        args: Parsed arguments containing id, title, and description.
        service: TaskService instance.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    task_id = args.id
    title = getattr(args, "title", None)
    description = getattr(args, "description", None)

    if title is None and description is None:
        print("Error: Must specify --title and/or --description", file=sys.stderr)
        return 1

    try:
        task = service.update_task(task_id, title=title, description=description)
        if task is None:
            print(f"Error: Task with ID {task_id} not found.", file=sys.stderr)
            return 1
        print(f"Task {task_id} updated successfully.")
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def handle_delete(args: argparse.Namespace, service: TaskService) -> int:
    """Handle the delete command.

    Args:
        args: Parsed arguments containing the task id.
        service: TaskService instance.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    task_id = args.id

    if service.delete_task(task_id):
        print(f"Task {task_id} deleted successfully.")
        return 0
    else:
        print(f"Error: Task with ID {task_id} not found.", file=sys.stderr)
        return 1


def handle_complete(args: argparse.Namespace, service: TaskService) -> int:
    """Handle the complete command.

    Args:
        args: Parsed arguments containing the task id.
        service: TaskService instance.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    task_id = args.id

    task = service.mark_complete(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found.", file=sys.stderr)
        return 1
    print(f"Task {task_id} marked as complete.")
    return 0


def handle_incomplete(args: argparse.Namespace, service: TaskService) -> int:
    """Handle the incomplete command.

    Args:
        args: Parsed arguments containing the task id.
        service: TaskService instance.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    task_id = args.id

    task = service.mark_incomplete(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found.", file=sys.stderr)
        return 1
    print(f"Task {task_id} marked as incomplete.")
    return 0
