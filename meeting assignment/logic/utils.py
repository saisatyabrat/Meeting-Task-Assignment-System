import re

def extract_deadline(sentence):
    deadlines = ["today","tomorrow","tonight","this week","next week",
                 "end of this week","Monday","Tuesday","Wednesday",
                 "Thursday","Friday","Saturday","Sunday","next Monday"]
    for d in deadlines:
        if d.lower() in sentence.lower():
            return d
    return None

def extract_priority(sentence):
    if "critical" in sentence.lower():
        return "Critical"
    if "high priority" in sentence.lower() or "important" in sentence.lower():
        return "High"
    if "medium" in sentence.lower():
        return "Medium"
    if "low" in sentence.lower():
        return "Low"
    return "Medium"
