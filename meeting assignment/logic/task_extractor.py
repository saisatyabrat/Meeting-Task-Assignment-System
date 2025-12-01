import re
from logic.utils import extract_deadline, extract_priority

def detect_tasks(text):
    lines = text.split(".")
    tasks = []

    for line in lines:
        if any(x in line.lower() for x in ["fix","update","design","write","optimize","create"]):
            task_desc = line.strip()

            deadline = extract_deadline(line)
            priority = extract_priority(line)

            assigned_to = None
            for name in ["Sakshi","Mohit","Arjun","Lata"]:
                if name.lower() in line.lower():
                    assigned_to = name

            tasks.append({
                "task": task_desc,
                "assigned_to": assigned_to,
                "deadline": deadline or "Not mentioned",
                "priority": priority,
                "dependencies": None,
                "reason": None
            })

    # detect dependencies
    for task in tasks:
        if "depends on" in task["task"].lower():
            task["dependencies"] = "Previous task"

    return tasks
