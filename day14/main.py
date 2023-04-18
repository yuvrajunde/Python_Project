# from functions import get_todos, write_todos
import functions
while True:
    user_action = input("Type add, show, edit  or Exit:")
    user_action = user_action.strip()
    if user_action.startswith("add"):
         todo = user_action[4:]
         todos = functions.get_todos("todos.txt")
         todos.append(todo + '\n')
         functions.write_todos(todos)

    elif 'show' in user_action:
        print(True)
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index+1}-{item}'
            print(row)
    elif user_action.startswith("edit"):
        try:
             numbers = int(user_action[5:])-1
             new = input("Enter new element")
             todos = functions.get_todos()
             todos[numbers] = new + '\n'
             functions.write_todos(todos)

             # todos[numbers] = new
             # write_todos("todos.txt",)
        except Exception as error:
            print("command is wrong")
            continue

    elif 'complete' in user_action:
         number = int(user_action[9:])
         todos = functions.get_todos()
         index = number - 1
         todo_to_remove = todos[index].strip('\n')
         todos.pop(index)
         functions.write_todos(todos)
         message = f"Todo {todo_to_remove} was removed from t he list"
    elif 'exit' in user_action:
        break
    else:
        print("command not valid")
print("Bye")