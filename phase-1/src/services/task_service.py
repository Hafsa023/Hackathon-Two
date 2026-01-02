"""Task service for managing todo tasks."""

from typing import Optional

from src.models.task import Task


class TaskServiceError(Exception):
    """Base exception for task service errors."""

    pass


class TaskNotFoundError(TaskServiceError):
    """Exception raised when a task is not found."""

    def __init__(self, task_id: int) -> None:
        """Initialize with the task ID that was not found."""
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found")


class TaskService:
    """Service for managing tasks in memory.

    Provides CRUD operations for tasks with auto-incrementing IDs.
    All tasks are stored in memory and lost when the application exits.
    """

    def __init__(self) -> None:
        """Initialize the TaskService with empty storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task with auto-assigned ID.

        Args:
            title: Short task title (1-100 characters).
            description: Optional detailed description.

        Returns:
            The created Task instance.

        Raises:
            ValueError: If title is empty or exceeds 100 characters.
        """
        # Validate title before creating task
        if not title:
            raise ValueError("Task title cannot be empty")
        if len(title) > 100:
            raise ValueError("Task title must be 100 characters or less")

        task = Task(id=self._next_id, title=title, description=description, status="incomplete")
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Return all tasks as a list.

        Returns:
            List of all tasks ordered by ID.
        """
        return [self._tasks[task_id] for task_id in sorted(self._tasks.keys())]

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            The Task if found, None otherwise.
        """
        return self._tasks.get(task_id)

    def update_task(
        self, task_id: int, title: Optional[str] = None, description: Optional[str] = None
    ) -> Optional[Task]:
        """Update a task's title and/or description.

        Args:
            task_id: The unique identifier of the task to update.
            title: New title (optional).
            description: New description (optional).

        Returns:
            The updated Task if found, None otherwise.

        Raises:
            ValueError: If title is empty or exceeds 100 characters.
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None

        if title is not None:
            if not title:
                raise ValueError("Task title cannot be empty")
            if len(title) > 100:
                raise ValueError("Task title must be 100 characters or less")
            task.title = title

        if description is not None:
            task.description = description

        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id: The unique identifier of the task to delete.

        Returns:
            True if the task was deleted, False if not found.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def mark_complete(self, task_id: int) -> Optional[Task]:
        """Mark a task as complete.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            The updated Task if found, None otherwise.
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None
        task.status = "complete"
        return task

    def mark_incomplete(self, task_id: int) -> Optional[Task]:
        """Mark a task as incomplete.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            The updated Task if found, None otherwise.
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None
        task.status = "incomplete"
        return task
