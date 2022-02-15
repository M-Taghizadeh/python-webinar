# Python Collections
#     list
#     tuple
#     set
#     dictionary


### LIST
### [DEFINE]
from math import prod


product = ['phone', 'laptop', 'car', 'apple', 'i dont know']


### [ACCESS ITEM]
print(product[1])
print(product[0:-1])


### [INSERT]
product.insert(2, 'mobile')


### [ADD] : append(), insert(), extend()
product.append("new product")


### [UPDATE]
product[1] = 'book'
product[1:3] = ["car", "paper"]


### [REMOVE]
# remove
product.remove('phone')


# del
del product[1]
del product
# clear
product.clear()
# pop
product.pop()


### [COPY]
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1 = l2 ### cal by reference
l1 = l2.copy()### cal by value


### [JOIN]
l1 = [10, 12, 13]
l2 = [1, 2]
new_list = l1 + l2
l1.extend(l2)
print(l1)


### [SORT]
sorted_list = sorted(l1)
print(sorted_list)


### [REVERSE]
l1.reverse()
print(l1)