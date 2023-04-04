
while True:
     user_action = input("Type add, show, edit  or Exit:")
     match user_action:
         case 'add':
             todo = input("Enter a todo") + "\n"
             with open("todos.txt","r") as file:
                 todos = file.readlines()
                 todos.append(todo)
             with open("todos.txt","w") as file:
                 file.writelines(todos)
             # file = open("todos.txt","w")
             print(file)

         case 'show' | 'display':
             file = open("todos.txt","r")
             todos = file.readlines()
             file.close()
             for index, item in enumerate(todos):
                 l = item.strip("\n")
                 print(index, l)
             file.close()
         case 'edit':
             numbers = int(input("Enter the index you want to edit"))
             new = input("Enter new element")
             with open("todos.txt","r") as file:
                 todos = file.readlines()
             todos[numbers] = new
             print(todos)
         case 'complete':
             number = int(input("Number of todo to complete:"))
             with open('todos.txt','r') as file:
                todos =  file.readlines()
             index = number - 1
             todo_to_remove = todos[index].strip('\n')
             todos.pop(index)
             with open('todos.txt','w') as file:
                 file.writelines(todos)
             message = f"Todo {todo_to_remove} was removed from the list"




         case 'exit':
             break
         case whatever:
             print("Hey, you entered a wrong command")
