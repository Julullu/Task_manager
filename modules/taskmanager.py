import json
import os
from modules.task import Task

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
DATA_FILE = os.path.join(DATA_DIR, 'tasks.json')

class TaskManager:
    def __init__ (self):
        self.tasks=[]

    def add_task(self, new_task):
        self.tasks.append(new_task)

    def get_all_tasks (self):
        return self.tasks
    
    def get_tasks_by_status (self,status):
        return [task for task in self.tasks if task.status== status]
    
    def update_task_status (self, task_id, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                if new_status in ["to-do", "in progress", "done"]:
                    task.status=new_status
                    return f"Stav úkolu {task_id} je: {task.status}"
                else:
                    return "Zadejte prosím platný stav tasku"
        return f"Task {task_id} se nepodařilo najít"
    
    def remove_task (self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.pop(task)
                return f"Task {task.task_id} byl odstraněn"
        return f" Task {task_id} se nepodařilo najít"
    
    def save_to_json (self, filename= DATA_FILE):
        with open (filename, "w", encoding ="utf-8") as file:
            json.dump ([TaskManager.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)
        return "Tasky byly uloženy"
    
    def load_from_json (self, filename = DATA_FILE):
        try:
            with open (filename, "r", encoding="utf-8") as file:
                data=json.load(file)
                self.tasks=[Task.from_dic(task_data) for task_data in data]
                return "Tasky byly načteny"
        except FileNotFoundError:
            return "Soubor neexistuje"
        except json.JSONDecodeError:
            return "Soubor nemá správnou json podobu"
        
    def __str__(self):

         return "\n".join(str(task) for task in self.tasks)

        