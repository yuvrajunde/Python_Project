def get_avg():
    with open("./data.txt", "r") as file:
        file = file.readlines()
    values = file[1:]
    sum = 0
    values = [float(i) for i in values]
    Max = f"Max:{max(values)}, Min:{min(values)}"
    return Max
    # for val in values:
    #     sum = sum + val
    # return sum/len(values)
temp = get_avg()
print(temp)