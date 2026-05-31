class Task:
    def __init__ (self, task_id, title, description, status="to-do"):
        self.task_id=task_id
        self.title=title
        self.description=description
        self.status=status
    
    def update_status(self, new_status):
        if new_status =="to_do":
            self.status="to-do"
        elif new_status=="in progress":
            self.status="in progress"
        elif new_status=="done":
            self.status="done"
        else:
            return"Zadejte platný stav projektu"
        return f"Stav objednávky:{self.status}"
    
    def name_change(self, new_name):
        self.title=new_name
        return f"Nové jméno projektu {self.task_id} je: {self.title}"
    
    def description_change (self, new_description):
        self.description=new_description
        return f"Nový popisek projektu {self.task_id} je: {self.description}"
    
    def to_dict(self):
        return {
            "task_id":self.task_id,
            "title":self.title,
            "description":self.description,
            "status": self.status
        }
    
    def from_dic (cls,dic):

        return cls(
            task_id= dic["task_id"],
            title= dic["title"],
            description= dic ["description"],
            status= dic["status"]
        )
    
    def __str__ (self):
        return f"Projekt #{self.task_id}: {self.title} | Popis: {self.description} | Stav: {self.status}"
