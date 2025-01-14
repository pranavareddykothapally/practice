
def  task():
    tasks = []
    print(f"___WELCOME TO THE TODO APP___")
    
    total_task = int(input("Enter the total number of task you want to add: "))
    
    for i in range(1,total_task+1):
        task_name = input(f"Enter the task {i}: ")
        tasks.append(task_name)
        
    print(f"Your task list is: ")
    while True:
        try:
            operation = int(input("Enter the operation you want to perform: \n1. Add a task\n2. Update a task\n3. Delete a task\n4. View all task\n5. Exit/Stop\n"))

            if operation == 1:
                add = input("Enter the task you want to add: ")
                tasks.append(add)
                print("Task {add} has been successfully to the list!")
            
            
            elif operation == 2:
                updated_task = input("Enter the task name you want to update = ")
                if updated_task in tasks:
                    up = input("Enter new task = ")
                    ind = tasks.index(updated_task)
                    tasks[ind] = up
                    print(f"Updated task '{updated_task}' to '{up}'.")
                else:
                    print("Task not found.")
        
        
            elif operation == 3:
                del_val = input("Which task you want to delete = ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task '{del_val}' has been deleted.")
                else:
                    print("Task not found.")
                
                
            elif operation == 4:
                print(f"Your To Do list is: {tasks}")
            
            
        
            elif operation == 5:
                print("Thank you for using the app!")
                break
            
        
            else:
                print("Invalid input! Please enter a number from 1 to 5.")
                
                
        except ValueError:
            print("Invalid Input. Please enter a valid number!")
            
task()
