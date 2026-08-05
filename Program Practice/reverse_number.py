number=int(input("Enter any number:"))

reverse=0

while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
    
print("Reverse Number:",reverse)