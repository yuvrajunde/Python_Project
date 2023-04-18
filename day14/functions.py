def get_todos(filepath="todos.txt"):
    """Read the file"""
    with open(filepath, "r") as file:
        return(file.readlines())
def write_todos(todos_args, filepath = "todos.txt"):
    "Write the file"
    with open(filepath, "w") as file:
        file.writelines(todos_args)

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
def getstate(input):
    if input < 0:
        return "Solid"
    elif input >= 0 and input <= 100:
        return "Liquid"
    else:
        return "Gas"


