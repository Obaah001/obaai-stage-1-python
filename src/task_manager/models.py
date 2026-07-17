# src/task_manager/models.py

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """
    Represents a single task in the task management system.

    Attributes:
        title (str): Short description of what needs to be done.
        description (str): Detailed explanation of the task.
        priority (str): Importance level — 'low', 'medium', or 'high'.
        status (str): Current state — 'pending', 'in_progress', or 'done'.
        task_id (str): Unique identifier, auto-generated.
        created_at (str): Timestamp of when the task was created.
        completed_at (Optional[str]): Timestamp of completion, or None.
    """
    title: str
    description: str
    priority: str = "medium"
    status: str = "pending"
    task_id: str = ""
    created_at: str = ""
    completed_at: Optional[str] = None

    VALID_PRIORITIES = ("low", "medium", "high")
    VALID_STATUSES = ("pending", "in_progress", "done")

    def __post_init__(self):
        if self.priority not in self.VALID_PRIORITIES:
            raise ValueError(
                f"Invalid priority '{self.priority}'. "
                f"Must be one of: {self.VALID_PRIORITIES}"
            )
        if self.status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid status '{self.status}'. "
                f"Must be one of: {self.VALID_STATUSES}"
            )
        if not self.title.strip():
            raise ValueError("Task title cannot be empty.")
        if not self.created_at:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_priority(self, new_priority: str) -> None:
        """
        Updates the task's priority to a new valid value.

        Args:
            new_priority (str): The new priority — 'low', 'medium', or 'high'.

        Raises:
            ValueError: If new_priority is not a valid priority level.
        """
        if new_priority not in self.VALID_PRIORITIES:
            raise ValueError(
                f"Invalid priority '{new_priority}'. "
                f"Must be one of: {self.VALID_PRIORITIES}."
            )
        self.priority = new_priority

    def mark_complete(self) -> None:
        """
        Marks the task as done and records the completion timestamp.
        """
        self.status = "done"
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def is_complete(self) -> bool:
        """
        Returns True if the task has been completed, False otherwise.
        """
        return self.status == "done"

    def to_dict(self) -> dict:
        """
        Converts the task to a dictionary for storage o`r API responses.
        """
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
        }

    def __str__(self) -> str:
        status_symbol = "✓" if self.is_complete() else "○"
        return (
            f"[{status_symbol}] {self.task_id} | {self.title} "
            f"| Priority: {self.priority} | Status: {self.status}"
        )