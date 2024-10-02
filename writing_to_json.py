import json

jobs = [
    {
        "title": "Data Scientist",
        "description": "Looking for a data scientist with expertise in machine learning and Python.",
        "skills_required": ["web development", "javascript"] 
    }
]

with open('jobs.json', 'w') as f:
    json.dump(jobs, f, indent=4)