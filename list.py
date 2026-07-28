numbers=[20,30,40,20,30,80,90,50,10,40,60]

sort1=[]

for i in numbers:
    if i not in sort1:
        sort1.append(i)

print(sort1)

sort1.sort()

print(sort1)