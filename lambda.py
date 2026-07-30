# def add(a,b):
#     return a+b

# print(add(10,30))

add=lambda a,b: a+b

print(add(10,20))


# Using map funtion with lambda
# # map basically do ,
# # if we are performing the the lambda function 
# on list then map function applies the lambda
# function to each element of the list


numbers=[2,3,4,5,6,8]

result=list(map(lambda x:x*x, numbers))

print(result)