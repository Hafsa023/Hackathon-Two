"""Menu-driven interface for the CLI Todo Application."""

import sys

from src.services.task_service import TaskService


def clear_screen() -> None:
    """Clear the terminal screen."""
    print("\n" * 2)


def display_menu() -> None:
    """Display the main menu."""
    print("=" * 50)
    print("          CLI TODO APPLICATION")
    print("=" * 50)
    print()
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete / Incomplete")
    print("6. Exit")
    print()
    print("-" * 50)


def get_menu_choice() -> int:
    """Get and validate menu choice from user.

    Returns:
        Integer choice between 1 and 6.
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-6): ").strip())
            if 1 <= choice <= 6:
                return choice
            print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_task_id(service: TaskService, prompt: str) -> int | None:
    """Get and validate a task ID from user.

    Args:
        service: TaskService instance.
        prompt: Prompt message for the user.

    Returns:
        Valid task ID or None if user cancels.
    """
    while True:
        try:
            task_id = int(input(prompt).strip())
            if task_id <= 0:
                print("Task ID must be a positive number.")
                continue
            task = service.get_task_by_id(task_id)
            if task is None:
                print(f"Task with ID {task_id} not found.")
                return None
            return task_id
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_title() -> str | None:
    """Get task title from user with validation.

    Returns:
        Valid title string or None if user cancels.
    """
    while True:
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            continue
        if len(title) > 100:
            print("Task title must be 100 characters or less.")
            continue
        return title


def get_optional_description() -> str:
    """Get optional description from user.

    Returns:
        Description string (empty if user skips).
    """
    desc = input("Enter task description (optional, press Enter to skip): ").strip()
    return desc


def menu_add_task(service: TaskService) -> None:
    """Handle Add Task menu option."""
    print("\n--- ADD TASK ---")
    title = get_title()
    if title is None:
        return

    description = get_optional_description()

    try:
        task = service.add_task(title, description)
        print(f"\nTask added successfully! (ID: {task.id})")
    except ValueError as e:
        print(f"\nError: {e}")


def menu_view_tasks(service: TaskService) -> None:
    """Handle View Tasks menu option."""
    print("\n--- VIEW TASKS ---")
    tasks = service.get_all_tasks()

    if not tasks:
        print("\nNo tasks found. Add a task to get started!")
        return

    print()
    print(f"{'ID':<5} {'Status':<14} {'Title':<30} {'Description'}")
    print("-" * 70)

    for task in tasks:
        status = "[Complete]  " if task.status == "complete" else "[Incomplete]"
        title = task.title[:28] + ".." if len(task.title) > 30 else task.title
        desc = task.description[:30] if task.description else ""

        print(f"{task.id:<5} {status:<14} {title:<30} {desc}")

    print()
    print(f"Total tasks: {len(tasks)}")
    print(f"  - Complete: {sum(1 for t in tasks if t.status == 'complete')}")
    print(f"  - Incomplete: {sum(1 for t in tasks if t.status == 'incomplete')}")


def menu_update_task(service: TaskService) -> None:
    """Handle Update Task menu option."""
    print("\n--- UPDATE TASK ---")
    tasks = service.get_all_tasks()

    if not tasks:
        print("\nNo tasks to update. Add a task first!")
        return

    print("\nCurrent tasks:")
    for task in tasks:
        status = "✔" if task.status == "complete" else "✖"
        print(f"  {task.id}. [{status}] {task.title}")

    task_id = get_task_id(service, "\nEnter task ID to update: ")
    if task_id is None:
        return

    task = service.get_task_by_id(task_id)
    print(f"\nCurrent: {task.title}")
    if task.description:
        print(f"         {task.description}")

    print("\nLeave fields empty to keep current value.")
    new_title = input("Enter new title (or press Enter to keep): ").strip()
    new_description = input("Enter new description (or press Enter to keep): ").strip()

    try:
        updated = service.update_task(
            task_id,
            title=new_title if new_title else None,
            description=new_description if new_description else None
        )
        if updated:
            print(f"\nTask {task_id} updated successfully!")
    except ValueError as e:
        print(f"\nError: {e}")


def menu_delete_task(service: TaskService) -> None:
    """Handle Delete Task menu option."""
    print("\n--- DELETE TASK ---")
    tasks = service.get_all_tasks()

    if not tasks:
        print("\nNo tasks to delete. Add a task first!")
        return

    print("\nCurrent tasks:")
    for task in tasks:
        status = "✔" if task.status == "complete" else "✖"
        print(f"  {task.id}. [{status}] {task.title}")

    task_id = get_task_id(service, "\nEnter task ID to delete: ")
    if task_id is None:
        return

    task = service.get_task_by_id(task_id)
    confirm = input(f"\nDelete task '{task.title}'? (y/n): ").strip().lower()

    if confirm == "y":
        if service.delete_task(task_id):
            print(f"\nTask {task_id} deleted successfully!")
        else:
            print(f"\nError: Could not delete task {task_id}.")


def menu_mark_complete(service: TaskService) -> None:
    """Handle Mark Complete menu option."""
    print("\n--- MARK TASK COMPLETE ---")
    tasks = service.get_all_tasks()

    if not tasks:
        print("\nNo tasks. Add a task first!")
        return

    incomplete_tasks = [t for t in tasks if t.status == "incomplete"]
    if not incomplete_tasks:
        print("\nAll tasks are already complete!")
        return

    print("\nIncomplete tasks:")
    for task in incomplete_tasks:
        print(f"  {task.id}. {task.title}")

    task_id = get_task_id(service, "\nEnter task ID to mark as complete: ")
    if task_id is None:
        return

    task = service.get_task_by_id(task_id)
    if task.status == "complete":
        print(f"\nTask {task_id} is already complete.")
        return

    if service.mark_complete(task_id):
        print(f"\nTask {task_id} marked as complete! ✓")


def menu_mark_incomplete(service: TaskService) -> None:
    """Handle Mark Incomplete menu option."""
    print("\n--- MARK TASK INCOMPLETE ---")
    tasks = service.get_all_tasks()

    if not tasks:
        print("\nNo tasks. Add a task first!")
        return

    complete_tasks = [t for t in tasks if t.status == "complete"]
    if not complete_tasks:
        print("\nNo complete tasks to mark as incomplete!")
        return

    print("\nComplete tasks:")
    for task in complete_tasks:
        print(f"  {task.id}. {task.title}")

    task_id = get_task_id(service, "\nEnter task ID to mark as incomplete: ")
    if task_id is None:
        return

    task = service.get_task_by_id(task_id)
    if task.status == "incomplete":
        print(f"\nTask {task_id} is already incomplete.")
        return

    if service.mark_incomplete(task_id):
        print(f"\nTask {task_id} marked as incomplete! ✖")


def menu_mark_toggle(service: TaskService) -> None:
    """Handle Mark Complete/Incomplete menu option with submenu."""
    while True:
        print("\n--- MARK TASK STATUS ---")
        print("1. Mark task as complete")
        print("2. Mark task as incomplete")
        print("3. Back to main menu")

        try:
            choice = int(input("\nEnter choice (1-3): ").strip())
            if choice == 1:
                menu_mark_complete(service)
                break
            elif choice == 2:
                menu_mark_incomplete(service)
                break
            elif choice == 3:
                return
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def run_menu(service: TaskService) -> None:
    """Run the main menu loop.

    Args:
        service: TaskService instance for task management.
    """
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            menu_add_task(service)
        elif choice == 2:
            menu_view_tasks(service)
        elif choice == 3:
            menu_update_task(service)
        elif choice == 4:
            menu_delete_task(service)
        elif choice == 5:
            menu_mark_toggle(service)
        elif choice == 6:
            print("\n" + "=" * 50)
            print("          Thank you for using Todo App!")
            print("                   Goodbye!")
            print("=" * 50)
            break

        # Pause before showing menu again
        input("\nPress Enter to continue...")


def main() -> int:
    """Main entry point for the menu-driven CLI application.

    Returns:
        Exit code (0 for success).
    """
    # Create task service (in-memory storage)
    service = TaskService()

    # Run the menu interface
    run_menu(service)

    return 0


if __name__ == "__main__":
    sys.exit(main())
