# date = input("Enter Todays date")
# rate = input("How do you rate your mood today from 1 to 10?")
# thought = input("Lets your thought flow\n")
# with open(f"../journal/{date}.txt", "w") as file:
#     file.write(thought+'/n')
#     file.write(mood)
#
while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")

