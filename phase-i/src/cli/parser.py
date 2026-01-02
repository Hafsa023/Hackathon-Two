"""Command-line argument parser for the todo application."""

import argparse
from typing import Optional


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the todo CLI.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple command-line todo application",
        epilog="Use 'todo <command> --help' for more information on a specific command.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="commands",
        description="Available commands",
        help="Command to execute",
    )

    # Add command
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new task",
        description="Add a new task to the todo list",
    )
    add_parser.add_argument("title", help="Task title (1-100 characters)")
    add_parser.add_argument(
        "description", nargs="?", default="", help="Optional task description"
    )

    # List command
    list_parser = subparsers.add_parser(
        "list",
        help="List all tasks",
        description="Display all tasks in the todo list",
    )

    # Update command
    update_parser = subparsers.add_parser(
        "update",
        help="Update a task",
        description="Update the title and/or description of an existing task",
    )
    update_parser.add_argument("id", type=int, help="Task ID to update")
    update_parser.add_argument("--title", help="New task title (1-100 characters)")
    update_parser.add_argument("--description", help="New task description")

    # Delete command
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a task",
        description="Remove a task from the todo list",
    )
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    # Complete command
    complete_parser = subparsers.add_parser(
        "complete",
        help="Mark a task as complete",
        description="Mark an existing task as complete",
    )
    complete_parser.add_argument("id", type=int, help="Task ID to mark as complete")

    # Incomplete command
    incomplete_parser = subparsers.add_parser(
        "incomplete",
        help="Mark a task as incomplete",
        description="Mark an existing task as incomplete",
    )
    incomplete_parser.add_argument("id", type=int, help="Task ID to mark as incomplete")

    return parser


def parse_args(args: Optional[list[str]] = None) -> argparse.Namespace:
    """Parse command-line arguments.

    Args:
        args: Optional list of arguments (defaults to sys.argv).

    Returns:
        Parsed namespace with command and arguments.
    """
    parser = create_parser()
    return parser.parse_args(args)
