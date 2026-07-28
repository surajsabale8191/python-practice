numbers=[20,30,40,20,30,80,90,50,10,40,60]

sort=[]

for i in numbers:
    if i not in sort:
        sort.append(i)

print(sort)