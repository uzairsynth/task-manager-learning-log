tasks = []


def add_task(name, deadline):
    task = {
        "name": name,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(task)


add_task("Finish robotic hand design", "2026-09-25")
add_task("Test thumb actuator", "2026-09-26")
add_task("Prepare progress report", "2026-09-27")


print(tasks)

def delete_task(task_index):
    tasks.pop(task_index)

    complete_task(0)
delete_task(1)

print(tasks)
