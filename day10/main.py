
while True:
    user_action = input("Type add, show, edit  or Exit:")
    user_action = user_action.strip()
    if user_action.startswith("add"):
         todo = user_action[4:] + '\n'
         with open("todos.txt","r") as file:
             todos = file.readlines()

             todos.append(todo)

         with open("todos.txt","w") as file:
             file.writelines(todos)

    elif 'show' in user_action:
        print(True)
        with open("todos.txt",'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index+1}-{item}'
            print(row)
    elif user_action.startswith("edit"):
        try:
             numbers = int(user_action[5:])-1
             new = input("Enter new element")

             with open("todos.txt","r") as file:
                 todos = file.readlines()

             todos[numbers] = new
        except Exception as error:
            print("command is wrong")
            continue

    elif 'complete' in user_action:
         number = int(user_action[9:])
         with open('todos.txt','r') as file:
            todos =  file.readlines()
         index = number - 1
         todo_to_remove = todos[index].strip('\n')
         todos.pop(index)
         with open('todos.txt','w') as file:
             file.writelines(todos)
         message = f"Todo {todo_to_remove} was removed from the list"
    elif 'exit' in user_action:
        break
    else:
        print("command not valid")
print("Bye")