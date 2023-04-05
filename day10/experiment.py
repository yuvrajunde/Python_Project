# try:
#     wid = float(input("Enter rectangle width:"))
#     len = float(input("Enter rectangle length:"))
#     if wid == len:
#         exit("Thats look like a square")
#     area= wid * leng
#     print(area)
# except ValueError:
#     print("wrong")
#

try:
    user_input = int(input("Enter total value:"))
    user_input > 0
    get_value = int(input("Enter value:"))
    percentage = (get_value*100)/user_input
    print(f"This is {percentage} %")
except ValueError:
    print("Error: enter a number")
