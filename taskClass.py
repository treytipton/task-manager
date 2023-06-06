class Task:
    def __init__(self,taskID,tTitle,tDescription,tDateAssigned,tDueDate):
        self.id = taskID
        self.title = tTitle
        self.description = tDescription
        self.dateAssigned = tDateAssigned
        self.dueDate = tDueDate
    
    def __str__(self):
        return f"{self.id},{self.title},{self.description},{self.dateAssigned},{self.dueDate}\n"
    
   
