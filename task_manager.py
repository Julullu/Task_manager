import os
from modules.task import Task
from modules.taskmanager import TaskManager

manager= TaskManager()
manager.load_from_json()

def print_menu():

    print("\n--- TASK MANAGER ---")
    print("1. Přidat úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Zobrazit úkoly podle stavu")
    print("4. Změnit stav úkolu")
    print("5. Změnit jméno úkolu")
    print("6. změnit popis úkolu")
    print("7. Smazat úkol")
    print("8. Uložit úkoly")
    print("9. Načíst úkoly")
    print("10. Konec programu")

def add_task():
    task_id = len(manager.get_all_orders()) + 1
    title=input("Zadejte název úkolu:")
    description=input("Zadejte popisek úkolu:")
    new_task=Task(task_id, title, description)
    manager.add_task(new_task)
    return "Task byl úspešně přidán"

def show_tasks():
    if not manager.get_all_tasks():
        print("Žádné objednávky zatím nebyly zadány.")
        return
    print("\n--- Seznam všech tasků---")
    print(manager)

def show_tasks_by_status ():
    status = input("Zadejte stav tasků ('to-do', 'in progress', 'done'): ")
    
    filtered_tasks = manager.get_tasks_by_status(status)

    if not filtered_tasks:
        print("Žádné tasky s tímto stavem nebyly nalezeny.")
        return

    print(f"\n--- Tasky se statusem '{status}' ---")
    for task in filtered_tasks:
        print(task)  

def name_change():
    try:
        task_id = int(input("Zadejte ID tasku ke změně jména: "))
        new_name = input("Zadejte nové jméno: ")
        Task.name_change(task_id, new_name)
    except ValueError:
        print("Chyba: ID tasku musí být číslo!")

def description_change():
    try:
        task_id = int(input("Zadejte ID tasku ke změně popisku: "))
        new_description = input("Zadejte nový popisek: ")
        Task.description_change(task_id, new_description)
    except ValueError:
        print("Chyba: ID tasku musí být číslo!")

def status_change():
    try:
        task_id = int(input("Zadejte ID tasku ke změně stavu: "))
        new_status = input("Zadejte nový stav ('to-do', 'in progress', 'done'): ")
        manager.update_task_status(task_id, new_status)
    except ValueError:
        print("Chyba: ID tasku musí být číslo!")

def remove_task():
    try:
        task_id=input("Zadejte id tasku, který chcete smazat:")
        manager.remove_task(task_id)
        return f"Task {task_id} byl úspěšně smazán"
    except ValueError:
        print("Chyba: ID tasku musí být číslo!")

def save():
    print(manager.save_to_json())

def load():
    print(manager.load_from_json())


while True:
    print_menu()

    choice = input("Vyberte akci (1-10): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks_by_status()
    elif choice == "4":
        name_change()
    elif choice == "5":
        description_change()
    elif choice == "6":
        status_change()()
    elif choice == "7":
        remove_task()
    elif choice == "8":
        save()
    elif choice == "9":
        load()
    elif choice == "10":
        print(manager.save_to_json())  
        print("Program byl ukončen.")
        break  
    else:
        print("Chyba: Neplatná volba, zkuste to znovu.")
