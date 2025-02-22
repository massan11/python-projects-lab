import os
import sys

todo_file = "todo_list.txt"

def load_tasks() -> list[str]:
    '''Load tasks from the to-do list file.'''
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]
        
def save_tasks(tasks: list[str]) -> None:
    '''Save tasks to the to-do list file.'''
    with open(todo_file, "w", encoding="utf-8") as file:
        file.writelines(task + "\n" for task in tasks)
        
def add_task(task_text: str) -> None:
    '''Add a task to the to-do list.'''
    tasks = load_tasks()
    if task_text in tasks:
        print(f"Task {task_text} already exists")
        return
    tasks.append(task_text)
    save_tasks(tasks)
    print(f"Task added: {task_text}")
    
def remove_task(task_text: str) -> None:
    '''Remove a task from the to-do list.'''
    tasks = load_tasks()
    if task_text not in tasks:
        print(f"Task {task_text} not found!")
        return
    tasks.remove(task_text)
    save_tasks(tasks)
    print(f"Task removed: {task_text}")
    
def list_tasks() -> None:
    '''List all tasks in the to-do list.'''
    tasks = load_tasks()
    if not tasks:
        print("No tasks found")
        return
    print("To-Do list:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}_{task}")
        
def clear_tasks() -> None:
    '''Clear all tasks from the to-do list.'''
    save_tasks([])
    print("All tasks cleared.")
    
def manage_tasks(action: str, task_text: str = None) -> None:
    '''Manage tasks based on the action provided.'''
    if action == "add" and task_text:
        add_task(task_text)
    elif action == "remove" and task_text:
        remove_task(task_text)
    elif action == "list":
        list_tasks()
    elif action == "clear":
        clear_tasks()
    else:
        print(f"Error: Invalid action '{action}'. Available actions: add, remove, list, clear.")
        sys.exit(1)