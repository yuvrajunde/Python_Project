#
# while True:
#      user_action = input("Type add, show, edit  or Exit:")
#      match user_action:
#          case 'add':
#              todo = input("Enter a todo") + "\n"
#
#              file = open("todos.txt","r")
#              todos = file.readlines()
#              file.close()
#              print(todos)
#              todos.append(todo)
#              file = open("todos.txt","w")
#              file.writelines(todos)
#              file.close()
#              print(file)
#
#          case 'show' | 'display':
#              file = open("todos.txt","r")
#              todos = file.readlines()
#              file.close()
#              for index, item in enumerate(todos):
#                  l = item.strip("\n")
#                  print(index, l)
#              file.close()
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


# filenames = ["1.doc", "1.report", "1.presentation"]
# newfilenames = [filenames.replace('.','-') + '.txt' for filenames in filenames]
# print(newfilenames)

# names = ["john smith", "jay santi", "eva kuki"]
# names = [names.title() for names in names]
# print(names)

# usernames = ["john 1990", "alberta1970", "magnola2000"]
# usernames = [len(usernames) for usernames in usernames]
# print(usernames)

user_entries = ['10', '19.1', '20']
user_entries = [float(user_entries) for user_entries in user_entries ]
print(sum(user_entries))