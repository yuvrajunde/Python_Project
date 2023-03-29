# todos = []
# while True:
#      user_action = input("Type add, show, edit  or Exit:")
#      match user_action:
#          case 'add':
#              todo = input("Enter a todo")
#              todos.append(todo)
#          case 'show' | 'display':
#              print(todos)
#              for item in todos:
#                  print(item)
#          case 'edit':
#              numbers = int(input("Enter the index you want to edit"))
#              new = input("Enter new element")
#              todos[numbers] = new
#              print(todos)
#
#          case 'exit':
#              break
#          case whatever:
#              print("Hey, you entered a wrong command")

# filenames = ["1.Rawdata.txt","1.Etldata.txt","1.Agrdata.txt"]
# new = []
# for f in filenames:
#     new.append(f.replace('.' ,'-',1))
# print(new)


# user_input = int(input("How many dollors have you got?"))
# amount = user_input * 0.95
# print(f"The values of euro become: {amount} ")

ranking = ["ram", "sham", "cham"]
user_input = input("enter a person name")
inde = ranking.index(user_input) + 1
print(inde)
