import json


tasks = [
    {
        "name": "Finish robotic hand design",
        "deadline": "2026-09-25",
        "completed": False
    },
    {
        "name": "Test thumb actuator",
        "deadline": "2026-09-26",
        "completed": True
    }
]


with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)


print("Tasks saved successfully")
with open("tasks.json", "r") as file:
    loaded_tasks = json.load(file)


print(loaded_tasks)