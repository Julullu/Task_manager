import pytest      
import time

from modules.task import Task
from modules.taskmanager import TaskManager

test_task=Task(1, "fyzika", "úlohy z Lepila")

def test_description_change():
    test_task.description_change("pracovní list")
    assert test_task.description == "pracovní list"

def test_invalid_task_status():
    result= test_task.update_status("neuděláno")
    assert result== "Zadejte platný stav projektu"

def test_name_change():
    test_task.name_change("physics")
    assert test_task.title == "physics"

def test_to_dic():
    result= test_task.to_dict
    assert result ==  {"task_id":1,"title": "fyzika","description":"úlohy z Lepila","status": "to-do"}

@pytest.fixture    
def sample_tasks():

    manager = TaskManager()
    task1 = Task(1, "svéčka", "něco z filozofie" )   
    task2 = Task(2, "matika", "něco ze stereometrie" )                  
    task3 = Task(3, "angličtina", "něco jednoduchého" )   

    manager.add_order(task1)
    manager.add_order(task2)
    manager.add_order(task3)
    return manager  

def test_add_task(sample_tasks):
    assert len(sample_tasks.get_all_tasks()) == 3

def test_get_tasks_by_status(sample_tasks):
    todo_tasks = sample_tasks.get_tasks_by_status("to-do")
    assert len(todo_tasks) == 3  

def test_update_task_status_valid(sample_tasks):

    sample_tasks.update_task_status(1, "in progress")
    assert sample_tasks.get_all_tasks()[0].status == "in progress"

def test_update_task_status_invalid(sample_tasks):
    result = sample_tasks.update_task_status(2, "unknown")
    assert sample_tasks.get_all_tasks()[1].status == "in progress"  
    assert result == "Neplatný stav objednávky!"

def test_update_nonexistent_task_in_populated_cafe(sample_tasks):
    result = sample_tasks.update_task_status(99, "done")
    assert result == "Chyba: Task s tímto ID neexistuje"


def test_task_workflow():

    manager = TaskManager()
    task = Task(7, "čeština", "něco do slohu")

    manager.add_task(task)
    assert len(manager.get_all_tasks()) == 1  

    task.update_task_status(7, "done")
    assert task.status == "done"       


def test_update_nonexistent_task_in_empty_manager():
    manager = TaskManager()  
    result = manager.update_task_status(999, "done")
    assert result == "Task 999 nebyl nalezen"


def test_large_task_list():
    manager = TaskManager()
    for i in range(1000):
        manager.add_task(Task(i, f"úkol {i}", "něco"))
    assert len(manager.get_all_tasks()) == 1000


def test_large_task_performance():
    manager = TaskManager()
    start_time = time.time() 

    for i in range(10000):
        manager.add_order(Task(i, f"úkol {i}", "něco" ))

    end_time = time.time()    
    assert end_time - start_time < 1.0  