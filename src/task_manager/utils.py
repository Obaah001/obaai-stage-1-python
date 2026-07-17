#src\task_manager\utils.py

from datetime import datetime

def get_current_timestamp() -> str:
    """_summary_
    Returns the current date and time as a formatted string.

    Returns:
        str: Timestamp in the format 'DD-MM-YYYY HH:MM"SS'

    Example:
    get_current_timestamp()
    '05-06-2026 9:24:39'
    """
    now = datetime.now()
    return now.strftime("%d-%m-%Y  %H:%M:%S")
    print

def format_task_id(task_number:  int) -> str:
    """_summary_
    converts a task number into a formatted task ID string

    Args:
        task_number (int): _description_
        A positve interger representing the task numbers

    Returns:
        str: _description_
        A fprmatted task ID like 'TASK-001'
    
    Raises:
        ValueError: if task_number is  less than 1

    Example:
    >>> format_task_id(1)
    'TASK-001'
    >>> format_task_id(43)
    'TASK-043'
    """

    if task_number < 1:
        raise ValueError(f"Task number must be at least 1. Got{task_number}")
    
    return f"TASK-{task_number:03d}"

def truncate_text(text: str , max_length: int = 50) -> str:
    """_summary_
        shorten a string to a maximum length adding'...'if truncated

    Args:
        text (str): the input string to truncate
        max_length (int, optional): the maximum length allowed. Defaults to 50.

    Returns:
        str: The original string if short enough, or a truncated one if long.

    Raises:
        ValuError: if the max_length is less than 4.

    Example:
    >>> truncate_text("Hello world", 5)
    'He...'
    >>> truncate_text("Hi", 50)
    'Hi'
    """

    if max_length < 4:
        raise ValueError(f"max_length must be at least 4. Got {max_length}")
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length - 3] + "..."
