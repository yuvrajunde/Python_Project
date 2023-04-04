user_input = input("Enter a password")
strong_password = False
digit = False
upper = False
if len(user_input) >= 8:
    strong_password = True
elif len(user_input) >= 7:
    strong_password = True

for i in user_input:
    if i.isdigit():
        digit = True
        strong_password = True
for i in user_input:
    if i.isupper():
        i.is
        upper = True
        strong_password = True
print(strong_password)
'length: 8 contains numbers, capital , letters and special sign '
