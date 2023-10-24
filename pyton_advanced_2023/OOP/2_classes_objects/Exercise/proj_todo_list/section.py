from project.task import Task


class Section:
    tasks = []

    def __init__(self, name: str):
        self.name = name

    def add_task(self, new_task: Task):
        if new_task.name not in [task.name for task in Section.tasks]:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'
        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str):
        for tskname in Section.tasks:
            if task_name == tskname.name:
                tskname.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        counter = 0
        for task in Section.tasks:
            if task.completed:
                Section.tasks.remove(task)
                counter += 1
        return f'Cleared {counter} tasks.'

    def view_section(self):
        result = [f'Section {self.name}:']
        for task in Section.tasks:
            task_details = f'{task.details()}'
            result.append(task_details)

        return '\n'.join(result)

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
