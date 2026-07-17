
# scratch.py — Foundation consolidation exercise

from datetime import datetime
from .models import Task


def create_task_report(tasks: list) -> str:
    """
    Takes a list of Task objects and returns a formatted report string.

    Args:
        tasks (list): A list of Task objects.

    Returns:
        str: A formatted summary of all tasks.
    """
    if not tasks:
        return "No tasks found."

    total = len(tasks)
    complete = 0
    pending = 0

    for task in tasks:
        if task.is_complete():
            complete += 1
        else:
            pending += 1

    report = f"--- Task Report ({datetime.now().strftime('%Y-%m-%d')}) ---\n"
    report += f"Total: {total} | Complete: {complete} | Pending: {pending}\n"
    report += "-" * 40 + "\n"

    for task in tasks:
        report += f"{task}\n"

    return report


if __name__ == "__main__":
    task_one = Task(
        title="Build ObaAi",
        description="The main mission",
        priority="high"
    )
    task_two = Task(
        title="Learn FastAPI",
        description="Stage 2",
        priority="medium"
    )
    task_three = Task(
        title="Set up PostgreSQL",
        description="Stage 3",
        priority="low"
    )

    task_one.mark_complete()

    all_tasks = [task_one, task_two, task_three]

    report = create_task_report(all_tasks)
    print(report)