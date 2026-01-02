"""Unit tests for the TaskService."""

import pytest

from src.models.task import Task
from src.services.task_service import TaskService


class TestTaskServiceAddTask:
    """Tests for TaskService.add_task method."""

    def test_add_task_creates_task_with_id_1(self) -> None:
        """Test that first added task gets ID 1."""
        service = TaskService()
        task = service.add_task("Buy milk", "Get 2% milk")
        assert task.id == 1
        assert task.title == "Buy milk"
        assert task.description == "Get 2% milk"
        assert task.status == "incomplete"

    def test_add_task_auto_increments_ids(self) -> None:
        """Test that task IDs auto-increment."""
        service = TaskService()
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        task3 = service.add_task("Task 3")
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_add_task_with_empty_description(self) -> None:
        """Test adding task without description."""
        service = TaskService()
        task = service.add_task("Buy milk")
        assert task.id == 1
        assert task.title == "Buy milk"
        assert task.description == ""
        assert task.status == "incomplete"

    def test_add_task_default_status_is_incomplete(self) -> None:
        """Test that new tasks default to incomplete status."""
        service = TaskService()
        task = service.add_task("Buy milk")
        assert task.status == "incomplete"

    def test_add_task_empty_title_raises_error(self) -> None:
        """Test that adding task with empty title raises ValueError."""
        service = TaskService()
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            service.add_task("")

    def test_add_task_title_too_long_raises_error(self) -> None:
        """Test that adding task with title > 100 chars raises ValueError."""
        service = TaskService()
        long_title = "x" * 101
        with pytest.raises(ValueError, match="Task title must be 100 characters or less"):
            service.add_task(long_title)


class TestTaskServiceGetAllTasks:
    """Tests for TaskService.get_all_tasks method."""

    def test_get_all_tasks_returns_empty_list_initially(self) -> None:
        """Test that new service returns empty list."""
        service = TaskService()
        assert service.get_all_tasks() == []

    def test_get_all_tasks_returns_all_tasks(self) -> None:
        """Test that get_all_tasks returns all added tasks."""
        service = TaskService()
        service.add_task("Task 1")
        service.add_task("Task 2")
        service.add_task("Task 3")
        tasks = service.get_all_tasks()
        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3


class TestTaskServiceGetTaskById:
    """Tests for TaskService.get_task_by_id method."""

    def test_get_task_by_id_existing(self) -> None:
        """Test getting an existing task by ID."""
        service = TaskService()
        service.add_task("Buy milk")
        task = service.get_task_by_id(1)
        assert task is not None
        assert task.id == 1
        assert task.title == "Buy milk"

    def test_get_task_by_id_not_found(self) -> None:
        """Test that getting non-existent task returns None."""
        service = TaskService()
        task = service.get_task_by_id(999)
        assert task is None


class TestTaskServiceUpdateTask:
    """Tests for TaskService.update_task method."""

    def test_update_task_title(self) -> None:
        """Test updating task title."""
        service = TaskService()
        service.add_task("Original title")
        updated = service.update_task(1, title="New title")
        assert updated is not None
        assert updated.title == "New title"

    def test_update_task_description(self) -> None:
        """Test updating task description."""
        service = TaskService()
        service.add_task("Buy milk")
        updated = service.update_task(1, description="Get eggs too")
        assert updated is not None
        assert updated.description == "Get eggs too"

    def test_update_task_both(self) -> None:
        """Test updating both title and description."""
        service = TaskService()
        service.add_task("Buy milk")
        updated = service.update_task(1, title="Buy eggs", description="Get 2 dozen")
        assert updated is not None
        assert updated.title == "Buy eggs"
        assert updated.description == "Get 2 dozen"

    def test_update_task_preserves_unmodified(self) -> None:
        """Test that update preserves unmodified fields."""
        service = TaskService()
        service.add_task("Buy milk", "Get milk")
        updated = service.update_task(1, title="Buy eggs")
        assert updated is not None
        assert updated.title == "Buy eggs"
        assert updated.description == "Get milk"
        assert updated.status == "incomplete"

    def test_update_task_not_found(self) -> None:
        """Test that updating non-existent task returns None."""
        service = TaskService()
        result = service.update_task(999, title="New title")
        assert result is None

    def test_update_task_empty_title_raises_error(self) -> None:
        """Test that updating with empty title raises ValueError."""
        service = TaskService()
        service.add_task("Buy milk")
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            service.update_task(1, title="")


class TestTaskServiceDeleteTask:
    """Tests for TaskService.delete_task method."""

    def test_delete_task_removes_task(self) -> None:
        """Test that delete removes the task."""
        service = TaskService()
        service.add_task("Buy milk")
        assert service.get_task_by_id(1) is not None
        result = service.delete_task(1)
        assert result is True
        assert service.get_task_by_id(1) is None

    def test_delete_task_not_found(self) -> None:
        """Test that deleting non-existent task returns False."""
        service = TaskService()
        result = service.delete_task(999)
        assert result is False

    def test_delete_task_preserves_other_tasks(self) -> None:
        """Test that deleting one task preserves others."""
        service = TaskService()
        service.add_task("Task 1")
        service.add_task("Task 2")
        service.add_task("Task 3")
        service.delete_task(2)
        tasks = service.get_all_tasks()
        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[1].id == 3


class TestTaskServiceMarkComplete:
    """Tests for TaskService.mark_complete method."""

    def test_mark_complete_changes_status(self) -> None:
        """Test that mark_complete changes status to complete."""
        service = TaskService()
        service.add_task("Buy milk")
        task = service.mark_complete(1)
        assert task is not None
        assert task.status == "complete"

    def test_mark_complete_idempotent(self) -> None:
        """Test that marking complete multiple times is idempotent."""
        service = TaskService()
        service.add_task("Buy milk")
        service.mark_complete(1)
        task = service.mark_complete(1)
        assert task is not None
        assert task.status == "complete"

    def test_mark_complete_not_found(self) -> None:
        """Test that marking complete non-existent task returns None."""
        service = TaskService()
        result = service.mark_complete(999)
        assert result is None


class TestTaskServiceMarkIncomplete:
    """Tests for TaskService.mark_incomplete method."""

    def test_mark_incomplete_changes_status(self) -> None:
        """Test that mark_incomplete changes status to incomplete."""
        service = TaskService()
        service.add_task("Buy milk")
        service.mark_complete(1)
        task = service.mark_incomplete(1)
        assert task is not None
        assert task.status == "incomplete"

    def test_mark_incomplete_idempotent(self) -> None:
        """Test that marking incomplete multiple times is idempotent."""
        service = TaskService()
        service.add_task("Buy milk")
        service.mark_complete(1)
        service.mark_incomplete(1)
        task = service.mark_incomplete(1)
        assert task is not None
        assert task.status == "incomplete"

    def test_mark_incomplete_not_found(self) -> None:
        """Test that marking incomplete non-existent task returns None."""
        service = TaskService()
        result = service.mark_incomplete(999)
        assert result is None
