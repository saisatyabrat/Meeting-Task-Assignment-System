import json

def load_team(path="data/team.json"):
    with open(path, "r") as f:
        return json.load(f)

def assign_tasks(tasks, team):
    for task in tasks:
        if task["assigned_to"] is not None:
            continue  # already mentioned in meeting

        desc = task["task"].lower()

        # match by skill
        if "ui" in desc or "design" in desc:
            task["assigned_to"] = "Arjun"

        elif "database" in desc or "backend" in desc or "api" in desc:
            task["assigned_to"] = "Mohit"

        elif "test" in desc or "qa" in desc:
            task["assigned_to"] = "Lata"

        else:
            task["assigned_to"] = "Sakshi"  # default frontend

    return tasks
