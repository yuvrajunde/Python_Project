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
#
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
#                  print(index, item)
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
#
# # filenames = ['document', 'report', 'presentation']
# # for index,j in enumerate(filenames):
# #     print(index,j)
#
# contents = ["India is my country", "All indians are brother and sister", "I love my country"]
# files = ["block.txt", "presentation.txt", "report.txt"]
# for content, filename in zip(contents,files):
#     file = open(f"../files/{filename}", "w")
#     file.write(content)
#
#
# a = "I am a boy " \
#     " from" \
#     " india"

# files = open("../files/essay.txt","r")
# data = files.read()
# print(len(data))

# user_input = input("Enter a name:") + "\n"
# files = open("../files/members.txt", "r")
# new = files.readlines()
#
# new.append(user_input)
# files = open("../files/members.txt", "w")
# files.writelines(new)

# filenames = ["block.txt", "presentation.txt", "report.txt"]
# for file in filenames:
#     file = open(f"../files/{file}","w")
#     file.write("Hello")
#     file.close()

filenames = ['a.txt', 'b.txt', 'c.txt']
for i in filenames:
    i = open(f"../files/{i}","r")
    s = i.read()
    print(s)
    i.close()

