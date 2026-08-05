# text=input("Enter a string:")
# rev=""
# for i in text:
#     rev=i+rev
    
    
# if text==rev:
#     print("string is Palindrom")
    
# else:
#     print("Not Pallindrom")
# # print(rev)
# # print(text)


num=int(input("Enter any number:"))
temp=num
rev=0

while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
    
    
if num==rev:
    print("Number is Pallindrom")
    
else:
    print("Number is not pallindrom")
