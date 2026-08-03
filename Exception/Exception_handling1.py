# try:
#     # Risky code

# except ExceptionType:
#     # Handle exception

# finally:
#     # Cleanup code (always runs)

try:
    print("Inside try")
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Inside finally")

print("Program Ended")