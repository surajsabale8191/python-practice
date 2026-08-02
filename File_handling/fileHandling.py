# file = open("Stud_Details.txt", "x")

# file=open("Stud_Details.txt", "w")

# file.write("Suraj Sabale")

# file.close()

with open("Stud_Details.txt", "r") as file:
    data = file.read()
    print(data)