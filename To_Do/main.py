todos = [{"id": 1, "name": "Cricket", "priority": 1, "status": "Not Completed"}]

def ShowToDos():
    if not todos:
        print("No Todo Added Yet")
        return
    
    for todo in todos:
        for key, value in todo.items():
            print(key, ":", value, end=' | ')
        print()
        
def AddToDO():
        name = input('Enter Task Name: ')
        priority = input('Enter Task priority: ')
        id = len(todos) + 1
        status = 'Not Completed'
        todo = {"id": id, "name": name, "priority": priority, "status": status}
        todos.append(todo)
    
def removeToDo():
    id = int(input('Enter id of ToDo: '))
    todos.pop(id-1)
    for todo in todos:
        if todo['id'] > id:
            todo['id'] = todo['id']-1;

def markAsCompleted():
    id = int(input('Enter ToDo id: '))
    for todo in todos:
        if todo['id'] == id:
            todo['status'] = "Completed"
    
while(True):
    choice = int(input(''' 
Choose one:
    1. Show All Todo
    2. Add Todo
    3. Remove Todo
    4. Mark as Completed
    5. Break
    '''))
    
    if(choice == 5):
        break
    
    def switch(choice):
        if(choice == 1):
            print("You Want to See All Todos")
            ShowToDos()
            
        elif(choice == 2):
            print("You Want to Add New Todo")
            AddToDO()
            print('Updated Todo List: ')
            ShowToDos()
            
        elif(choice == 3):
            print("You Want to Remove Todo")
            removeToDo()
            print('Updated Todo List: ')
            ShowToDos()
            
        elif(choice == 4):
            print("You Want to Mark Todo As Completed")
            markAsCompleted()
            print('Updated Todo List: ')
            ShowToDos()
    
    switch(choice)


