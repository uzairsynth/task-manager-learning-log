tasks = [
    {
        "name": "Finish robotic hand design",
        "deadline": "2026-09-25",
        "completed": False
    },
    {
        "name": "Test thumb actuator",
        "deadline": "2026-09-26",
        "completed": False
    },
    {
        "name": "Prepare progress report",
        "deadline": "2026-09-27",
        "completed": True
    }
]

print(tasks)
for task in tasks:
    print(task["name"])