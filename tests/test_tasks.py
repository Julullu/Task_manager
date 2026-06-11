import pytest      

from modules.task import Task

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

