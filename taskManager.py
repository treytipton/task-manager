import csv;
import datetime;
import taskClass

currentTask = 'currentTasks.csv'
completedTask = 'completedTasks.csv'

def getNewID(file):
    with open(file,"r") as taskList:
        data = list(csv.reader(taskList))
    length = len(data)
    if(length > 0):
        return int(data[length-1][0]) + 1
    else:
        return 1

def newTask():
    tID = getNewID(currentTask)
    tTitle = input("Enter a title of your task: ")
    tDescription = input("Give a description for your task: ")
    tDateCreated = datetime.date.today()
    dueDateCreated = False
    while dueDateCreated == False:
        dueDateString = input("Enter the due date (MM-DD-YYYY): ")
        try:
            tDueDate = datetime.datetime.strptime(dueDateString, "%m-%d-%Y").date()
            dueDateCreated = True
        except:
            print("Invalid date format: Try again with the format (MM-DD-YYYY).")
    new_task = taskClass.Task(tID, tTitle, tDescription, tDateCreated, tDueDate)
    currentTasks = open(currentTask,'a')
    currentTasks.write(str(new_task))
    currentTasks.close()
    return
    

def viewTasks():
    with open(currentTask,'r') as taskList:
        data = list(csv.reader(taskList))
    length = len(data)
    print("ID | Title | Date Assigned | Due Date\n")
    for line in data:
        print(line[0],"  ",line[1],"  ",line[3],"  ",line[4],"\n")
    
def completeTask():
    with open(currentTask,'r') as taskList:
        data = list(csv.reader(taskList))
    if len(data) == 0:
        print("Completed task list empty, please try something else.")
        return
    
    viewTasks()
    taskToComplete = input("Which task would you like to complete?")
    for line in data:
        if line[0] == taskToComplete:
            lineToChange = line
    if len(lineToChange) == 0:
        print("No task with that ID found.")
        return
    
    fCompleted = open("completedTasks.csv","a")
    fCompleted.write(str(lineToChange) + "\n")
    fCompleted.close()
    
    with open("currentTasks.csv","w") as taskList:
        taskList.truncate(0)
    
    current = open("currentTasks.csv","a")
    for line in data:
        if line != lineToChange:
            current.write(line + "\n")
            
def viewCompleted():
    with open(completedTask,'r') as taskList:
        data = list(csv.reader(taskList))
    length = len(data)
    print("ID | Title | Date Assigned | Due Date\n")
    
    characters_to_filter = "[]'"

    translation_table = str.maketrans("", "", characters_to_filter)

    for line in data:
        filtered_line = [str(elem).translate(translation_table) for elem in line]
        print(filtered_line[0], "  ", filtered_line[1], "  ", filtered_line[3], "  ", filtered_line[4], "\n")


def deleteTask():
    fileToOpen = input("Which list do you want to delete a task from?\n1. Current Tasks\n2.Completed Tasks\n")
    if fileToOpen == '1':
        viewTasks()
        filePath = currentTask
        with open(currentTask,'r') as taskList:
            data = list(csv.reader(taskList))
    elif fileToOpen == '2':
        viewCompleted()
        filePath = completedTask
        with open(completedTask,'r') as taskList:
            data = list(csv.reader(taskList))
    else:
        print("No option selected, returning to home screen.")
        return
    taskToDelete = input("Which task would you like to delete?")
    for line in data:
        if line[0] == taskToDelete:
            lineToChange = line
    if len(lineToChange) == 0:
        print("No task with that ID found.")
        return
    
    with open(filePath,"w") as taskList:
        taskList.truncate(0)
    
    actualFile = open(filePath,"a")
    for line in data:
        if line != lineToChange:
            actualFile.write(str(line) + "\n")
    return
    
def exitProgram():
    print("You exited the program.")

options = {
    '1':newTask,
    '2':viewTasks,
    '3':completeTask,
    '4':viewCompleted,
    '5':deleteTask,
    '6':exitProgram
}

def executeCommand(command):
    if command in options:
        options[command]
    else:
        print("Error: Choice not listed, please try again.")

def main():
    while True:
        command = input("What would you like to do?:\n1. Add a task\n2. View task list\n3. Mark a task completed\n4. View completed tasks\n5. Delete a task\n6. Exit program\n")
        options[command]()  # Call the function by adding parentheses
        if command == '6':
            break
        
main()