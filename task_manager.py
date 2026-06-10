import os
from modules.task import Task
from modules.taskmanager import TaskManager

LOG_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'TaskManager',
    'log'
)

LOG_FILE = os.path.join(LOG_DIR, "task_manager.log")
LOG_ENABLED = True

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

manager = TaskManager()
manager.load_from_json()


def print_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Přidat úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Zobrazit úkoly podle stavu")
    print("4. Změnit stav úkolu")
    print("5. Změnit jméno úkolu")
    print("6. Změnit popis úkolu")
    print("7. Smazat úkol")
    print("8. Uložit úkoly")
    print("9. Načíst úkoly")
    print("10. Konec programu")


def add_task():
    task_id = len(manager.get_all_tasks()) + 1

    title = input("Zadejte název úkolu: ")
    description = input("Zadejte popisek úkolu: ")

    new_task = Task(task_id, title, description)
    manager.add_task(new_task)

    print("Task byl úspěšně přidán.")


def show_tasks():
    tasks = manager.get_all_tasks()

    if not tasks:
        print("Žádné úkoly zatím nebyly zadány.")
        return

    print("\n--- Seznam všech tasků ---")
    for task in tasks:
        print(task)


def show_tasks_by_status():
    status = input("Zadejte stav ('to-do', 'in progress', 'done'): ")

    filtered_tasks = manager.get_tasks_by_status(status)

    if not filtered_tasks:
        print("Žádné tasky s tímto stavem nebyly nalezeny.")
        return

    print(f"\n--- Tasky se statusem '{status}' ---")
    for task in filtered_tasks:
        print(task)


def status_change():
    try:
        task_id = int(input("Zadejte ID tasku ke změně stavu: "))
        new_status = input(
            "Zadejte nový stav ('to-do', 'in progress', 'done'): "
        )

        manager.update_task_status(task_id, new_status)
        print("Status byl změněn.")

    except ValueError:
        print("Chyba: ID tasku musí být číslo!")


def name_change():
    try:
        task_id = int(input("Zadejte ID tasku ke změně jména: "))
        new_name = input("Zadejte nové jméno: ")

        # Musí existovat odpovídající metoda v TaskManageru
        manager.update_task_name(task_id, new_name)

        print("Jméno bylo změněno.")

    except ValueError:
        print("Chyba: ID tasku musí být číslo!")


def description_change():
    try:
        task_id = int(input("Zadejte ID tasku ke změně popisku: "))
        new_description = input("Zadejte nový popisek: ")

        # Musí existovat odpovídající metoda v TaskManageru
        manager.update_task_description(task_id, new_description)

        print("Popisek byl změněn.")

    except ValueError:
        print("Chyba: ID tasku musí být číslo!")


def remove_task():
    try:
        task_id = int(input("Zadejte ID tasku, který chcete smazat: "))

        manager.remove_task(task_id)

        print(f"Task {task_id} byl úspěšně smazán.")

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
        status_change()

    elif choice == "5":
        name_change()

    elif choice == "6":
        description_change()

    elif choice == "7":
        remove_task()

    elif choice == "8":
        save()

    elif choice == "9":
        load()

    elif choice == "10":
        manager.save_to_json()
        print("Program byl ukončen.")
        break

    else:
        print("Chyba: Neplatná volba, zkuste to znovu.")