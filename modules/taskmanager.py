import json
import os
from modules.task import Task

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DATA_FILE = os.path.join(DATA_DIR, "tasks.json")

os.makedirs(DATA_DIR, exist_ok=True)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, new_task):
        self.tasks.append(new_task)

    def get_all_tasks(self):
        return self.tasks

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.task_id == task_id:

                if new_status in ["to-do", "in progress", "done"]:
                    task.status = new_status
                    return f"Stav úkolu {task_id} byl změněn na {new_status}"

                return "Zadejte platný stav ('to-do', 'in progress', 'done')"

        return f"Task {task_id} nebyl nalezen"

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return f"Task {task_id} byl odstraněn"

        return f"Task {task_id} nebyl nalezen"

    def save_to_json(self, filename=DATA_FILE):

        try:
            with open(filename, "w", encoding="utf-8") as file:

                json.dump(
                    [task.to_dict() for task in self.tasks],
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            return "Tasky byly uloženy"

        except Exception as e:
            return f"Chyba při ukládání: {e}"

    def load_from_json(self, filename=DATA_FILE):

        try:

            if not os.path.exists(filename):
                self.tasks = []
                return "Soubor neexistuje"
            

            with open(filename, "r", encoding="utf-8") as file:

                data = json.load(file)

                self.tasks = [
                    Task.from_dict(task_data)
                    for task_data in data
                ]

            return "Tasky byly načteny"

        except json.JSONDecodeError:
            self.tasks = []
            return "Soubor obsahuje neplatný JSON"

        except PermissionError:
            return (
                f"Nemám oprávnění otevřít soubor:{filename}"
            )

        except Exception as e:
            return f"Neočekávaná chyba: {e}"

    def __str__(self):
        if not self.tasks:
            return "Žádné tasky."

        return "\n".join(str(task) for task in self.tasks)