# todos = []
# while True:
#      user_action = input("Type add, show, edit  or Exit:")
#      match user_action:
#          case 'add':
#              todo = input("Enter a todo")
#              todos.append(todo)
#          case 'show' | 'display':
#              print(todos)
#              for index, item in enumerate(todos):
#                  print(index, item)
#          case 'edit':
#              numbers = int(input("Enter the index you want to edit"))
#              new = input("Enter new element")
#              todos[numbers] = new
#              print(todos)
#          case 'complete':
#              number = int(input("Number of todo to complete:"))
#              todos.pop(number)
#
#
#          case 'exit':
#              break
#          case whatever:
#              print("Hey, you entered a wrong command")

# filenames = ['document', 'report', 'presentation']
# for index,j in enumerate(filenames):
#     print(index,j)

ips = ['100.122.133.105', '100.122.133.111']
user_input = int(input("Enter the index you want:"))
print(ips[user_input])