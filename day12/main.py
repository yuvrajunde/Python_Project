def get_todos(filepath):
    with open(filepath, "r") as file:
        return(file.readlines())

def write_todos(filepath, todos_args):
    with open(filepath, "w") as file:
        file.writelines(todos_args)


while True:
    user_action = input("Type add, show, edit  or Exit:")
    user_action = user_action.strip()
    if user_action.startswith("add"):
         todo = user_action[4:]
         todos = get_todos("todos.txt")
         todos.append(todo + '\n')
         write_todos("todos.txt",todos)

    elif 'show' in user_action:
        print(True)
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index+1}-{item}'
            print(row)
    elif user_action.startswith("edit"):
        try:
             numbers = int(user_action[5:])-1
             new = input("Enter new element")
             todos = get_todos("todos.txt")
             todos[numbers] = new + '\n'
             write_todos("todos.txt",todos)

             # todos[numbers] = new
             # write_todos("todos.txt",)
        except Exception as error:
            print("command is wrong")
            continue

    elif 'complete' in user_action:
         number = int(user_action[9:])
         todos = get_todos("todos.txt")
         index = number - 1
         todo_to_remove = todos[index].strip('\n')
         todos.pop(index)
         write_todos("todos.txt",todos)
         message = f"Todo {todo_to_remove} was removed from t he list"
    elif 'exit' in user_action:
        break
    else:
        print("command not valid")
print("Bye")