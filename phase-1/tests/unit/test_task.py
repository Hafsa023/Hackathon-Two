"""Unit tests for the Task model."""

import pytest

from src.models.task import Task


class TestTaskInitialization:
    """Tests for Task initialization."""

    def test_create_task_with_all_fields(self) -> None:
        """Test creating a task with all fields specified."""
        task = Task(id=1, title="Buy milk", description="Get 2% milk", status="incomplete")
        assert task.id == 1
        assert task.title == "Buy milk"
        assert task.description == "Get 2% milk"
        assert task.status == "incomplete"

    def test_create_task_with_default_description(self) -> None:
        """Test creating a task with default empty description."""
        task = Task(id=1, title="Buy milk")
        assert task.id == 1
        assert task.title == "Buy milk"
        assert task.description == ""
        assert task.status == "incomplete"

    def test_create_task_with_default_status(self) -> None:
        """Test creating a task with default incomplete status."""
        task = Task(id=1, title="Buy milk")
        assert task.status == "incomplete"

    def test_create_task_with_complete_status(self) -> None:
        """Test creating a task with complete status."""
        task = Task(id=1, title="Buy milk", status="complete")
        assert task.status == "complete"


class TestTaskValidation:
    """Tests for Task field validation."""

    def test_title_cannot_be_empty(self) -> None:
        """Test that empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(id=1, title="")

    def test_title_cannot_exceed_max_length(self) -> None:
        """Test that title exceeding 100 characters raises ValueError."""
        long_title = "x" * 101
        with pytest.raises(ValueError, match="Task title must be 100 characters or less"):
            Task(id=1, title=long_title)

    def test_title_exactly_100_chars_is_valid(self) -> None:
        """Test that title with exactly 100 characters is valid."""
        title = "x" * 100
        task = Task(id=1, title=title)
        assert len(task.title) == 100

    def test_invalid_status_raises_value_error(self) -> None:
        """Test that invalid status raises ValueError."""
        with pytest.raises(ValueError, match="Task status must be 'incomplete' or 'complete'"):
            Task(id=1, title="Buy milk", status="pending")

    def test_invalid_id_raises_value_error(self) -> None:
        """Test that invalid ID raises ValueError."""
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            Task(id=0, title="Buy milk")

    def test_negative_id_raises_value_error(self) -> None:
        """Test that negative ID raises ValueError."""
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            Task(id=-1, title="Buy milk")


class TestTaskProperties:
    """Tests for Task property getters and setters."""

    def test_set_valid_title(self) -> None:
        """Test setting a valid title."""
        task = Task(id=1, title="Buy milk")
        task.title = "Buy eggs"
        assert task.title == "Buy eggs"

    def test_set_empty_title_raises_error(self) -> None:
        """Test that setting empty title raises ValueError."""
        task = Task(id=1, title="Buy milk")
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            task.title = ""

    def test_set_title_too_long_raises_error(self) -> None:
        """Test that setting too long title raises ValueError."""
        task = Task(id=1, title="Buy milk")
        with pytest.raises(ValueError, match="Task title must be 100 characters or less"):
            task.title = "x" * 101

    def test_set_description(self) -> None:
        """Test setting description."""
        task = Task(id=1, title="Buy milk")
        task.description = "Get 2% milk from store"
        assert task.description == "Get 2% milk from store"

    def test_set_status_to_complete(self) -> None:
        """Test setting status to complete."""
        task = Task(id=1, title="Buy milk", status="incomplete")
        task.status = "complete"
        assert task.status == "complete"

    def test_set_status_to_incomplete(self) -> None:
        """Test setting status to incomplete."""
        task = Task(id=1, title="Buy milk", status="complete")
        task.status = "incomplete"
        assert task.status == "incomplete"

    def test_set_invalid_status_raises_error(self) -> None:
        """Test that setting invalid status raises ValueError."""
        task = Task(id=1, title="Buy milk")
        with pytest.raises(ValueError, match="Task status must be 'incomplete' or 'complete'"):
            task.status = "invalid"


class TestTaskEquality:
    """Tests for Task equality and hashing."""

    def test_equal_tasks_same_id(self) -> None:
        """Test that tasks with same ID are equal."""
        task1 = Task(id=1, title="Buy milk")
        task2 = Task(id=1, title="Different title", status="complete")
        assert task1 == task2

    def test_different_tasks_different_id(self) -> None:
        """Test that tasks with different IDs are not equal."""
        task1 = Task(id=1, title="Buy milk")
        task2 = Task(id=2, title="Buy milk")
        assert task1 != task2

    def test_task_not_equal_to_non_task(self) -> None:
        """Test that Task is not equal to non-Task objects."""
        task = Task(id=1, title="Buy milk")
        assert task != "not a task"
        assert task != 1
        assert task != None

    def test_task_hash_based_on_id(self) -> None:
        """Test that Task hash is based on ID."""
        task1 = Task(id=1, title="Buy milk")
        task2 = Task(id=1, title="Different title")
        assert hash(task1) == hash(task2)

    def test_task_in_set(self) -> None:
        """Test that Task can be used in a set."""
        task1 = Task(id=1, title="Buy milk")
        task2 = Task(id=1, title="Different title")
        task_set = {task1, task2}
        assert len(task_set) == 1  # Same ID, so only one in set


class TestTaskRepr:
    """Tests for Task __repr__ method."""

    def test_repr_contains_all_fields(self) -> None:
        """Test that __repr__ contains all important fields."""
        task = Task(id=1, title="Buy milk", description="Get milk", status="incomplete")
        repr_str = repr(task)
        assert "Task" in repr_str
        assert "id=1" in repr_str
        assert "Buy milk" in repr_str
        assert "Get milk" in repr_str
        assert "incomplete" in repr_str


class TestTaskToDict:
    """Tests for Task to_dict method."""

    def test_to_dict_returns_all_fields(self) -> None:
        """Test that to_dict returns all task fields."""
        task = Task(id=1, title="Buy milk", description="Get milk", status="complete")
        result = task.to_dict()
        assert result == {
            "id": 1,
            "title": "Buy milk",
            "description": "Get milk",
            "status": "complete",
        }

    def test_to_dict_with_default_fields(self) -> None:
        """Test to_dict with default description and status."""
        task = Task(id=1, title="Buy milk")
        result = task.to_dict()
        assert result == {
            "id": 1,
            "title": "Buy milk",
            "description": "",
            "status": "incomplete",
        }
