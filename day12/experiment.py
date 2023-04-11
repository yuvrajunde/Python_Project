# feet_inches = input("Enter feet and inches:")
# def convert(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
# result  = convert(feet_inches)
#
# if result < 1:
#     print("Kid is small")
# else:
#     print("Kid can use the slide")

# user = int(input("enter liter"))
# def meter(value):
#     m = value / 1000
#     return m
# print(meter(user))

user = input("Enter a pass:")

user_password = input("Enter new password: ")


def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(strength(user_password))

