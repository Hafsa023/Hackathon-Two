"""Task entity model for the CLI Todo Application."""


class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique integer identifier for the task.
        title: Short description of the task (1-100 characters).
        description: Optional detailed description of the task.
        status: Completion status, either 'incomplete' or 'complete'.
    """

    MIN_TITLE_LENGTH = 1
    MAX_TITLE_LENGTH = 100

    def __init__(self, id: int, title: str, description: str = "", status: str = "incomplete") -> None:
        """Initialize a Task instance.

        Args:
            id: Unique identifier for the task.
            title: Short task title (1-100 characters).
            description: Optional detailed description.
            status: Task status, defaults to 'incomplete'.

        Raises:
            ValueError: If title is empty or exceeds 100 characters.
            ValueError: If status is not 'incomplete' or 'complete'.
        """
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not isinstance(title, str):
            raise ValueError("Task title must be a string")

        if len(title) < self.MIN_TITLE_LENGTH:
            raise ValueError("Task title cannot be empty")

        if len(title) > self.MAX_TITLE_LENGTH:
            raise ValueError(f"Task title must be {self.MAX_TITLE_LENGTH} characters or less")

        if status not in ("incomplete", "complete"):
            raise ValueError("Task status must be 'incomplete' or 'complete'")

        self._id = id
        self._title = title
        self._description = description
        self._status = status

    @property
    def id(self) -> int:
        """Return the task's unique identifier."""
        return self._id

    @property
    def title(self) -> str:
        """Return the task's title."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Set the task's title with validation.

        Args:
            value: New title value.

        Raises:
            ValueError: If title is empty or exceeds 100 characters.
        """
        if not isinstance(value, str):
            raise ValueError("Task title must be a string")

        if len(value) < self.MIN_TITLE_LENGTH:
            raise ValueError("Task title cannot be empty")

        if len(value) > self.MAX_TITLE_LENGTH:
            raise ValueError(f"Task title must be {self.MAX_TITLE_LENGTH} characters or less")

        self._title = value

    @property
    def description(self) -> str:
        """Return the task's description."""
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """Set the task's description."""
        if not isinstance(value, str):
            raise ValueError("Task description must be a string")
        self._description = value

    @property
    def status(self) -> str:
        """Return the task's completion status."""
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        """Set the task's status.

        Args:
            value: New status value ('incomplete' or 'complete').

        Raises:
            ValueError: If status is not 'incomplete' or 'complete'.
        """
        if value not in ("incomplete", "complete"):
            raise ValueError("Task status must be 'incomplete' or 'complete'")
        self._status = value

    def __repr__(self) -> str:
        """Return a string representation of the Task for debugging."""
        return f"Task(id={self._id!r}, title={self._title!r}, description={self._description!r}, status={self._status!r})"

    def __eq__(self, other: object) -> bool:
        """Check equality based on task ID.

        Args:
            other: Object to compare with.

        Returns:
            True if other is a Task with the same ID, False otherwise.
        """
        if not isinstance(other, Task):
            return NotImplemented
        return self._id == other._id

    def __hash__(self) -> int:
        """Return hash based on task ID for use in collections."""
        return hash(self._id)

    def to_dict(self) -> dict:
        """Convert the Task to a dictionary representation.

        Returns:
            Dictionary with task data.
        """
        return {
            "id": self._id,
            "title": self._title,
            "description": self._description,
            "status": self._status,
        }
