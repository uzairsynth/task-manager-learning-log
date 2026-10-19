class Task:

    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.completed = False

    def complete(self):
        self.completed = True


task1 = Task("Finish robotic hand design", "2026-09-25")

print(task1.completed)

task1.complete()

print(task1.completed)