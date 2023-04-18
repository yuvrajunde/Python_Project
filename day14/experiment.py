# from functions import parse,convert
#
# feet_inches = input("Enter feet and inches:")
#
# parsed = parse(feet_inches)
# result  = convert(parsed['feet'], parsed['inches'])
# print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")
#
#
# if result < 1:
#     print("Kid is small")
# else:
#     print("Kid can use the slide")
#
# user = int(input("enter liter"))
from functions import getstate
user_input = int(input("Enter Water Temp:"))

temp = getstate(user_input)
print(temp)
