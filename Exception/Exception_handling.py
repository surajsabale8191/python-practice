# try:
#     print("Python")
#     print(20 / 4)

# except ZeroDivisionError:
#     print("Error")

# else:
#     print("Success")

# print("End")


try:
    print("Start")
    print(20 / 0)

except ZeroDivisionError:
    print("Handled")

else:
    print("Success")

print("Finish")