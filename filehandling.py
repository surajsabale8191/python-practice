# # file = open("Student.txt","w")
# # file.write("Age: 22")
# # file.write("Course: Python")


# # file.close()

# # print("Data witten successfully.")
# # import time
# # file = open("student.txt", "r")

# # data = file.read()

# # print(data)
# # time.sleep(3)
# # file.close()

# # file=open("Student.txt","a")

# # file.write("City: Pune")

# # file.close()

# # print("data appended succesfully")

# with open("student.txt", "r") as file:
#     print(file.read())

import os

if os.path.exists("student.txt"):
    print("File exists")
else:
    print("File not found")