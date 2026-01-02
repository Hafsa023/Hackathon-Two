"""Main entry point for the CLI Todo Application."""

import sys

from src.cli.parser import parse_args
from src.cli.commands import (
    handle_add,
    handle_list,
    handle_update,
    handle_delete,
    handle_complete,
    handle_incomplete,
)
from src.services.task_service import TaskService


def main() -> int:
    """Main entry point for the todo CLI application.

    Returns:
        Exit code (0 for success, non-zero for error).
    """
    # Parse command-line arguments
    args = parse_args()

    # Create task service (in-memory storage)
    service = TaskService()

    # Route to appropriate command handler
    command_handlers = {
        "add": handle_add,
        "list": handle_list,
        "update": handle_update,
        "delete": handle_delete,
        "complete": handle_complete,
        "incomplete": handle_incomplete,
    }

    handler = command_handlers.get(args.command)
    if handler is None:
        print("Error: Unknown command. Use 'todo --help' for usage.", file=sys.stderr)
        return 1

    return handler(args, service)


if __name__ == "__main__":
    sys.exit(main())
