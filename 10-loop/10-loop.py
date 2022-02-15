# Python has two primitive loop commands:
#   while loops
#   for loops

i = 0
while i < 10:
    print(i)
    i += 1
else: print("i is no longer less than 10")


# break : stop the loop even if the while condition is true
i = 0
while i < 10:
    if i == 3:
        break
    print(i)
    i += 1


# continue : stop the current iteration, and continue with the next
i = 0
while i < 10:
    if i == 3:
        i += 1 
        continue
    print(i)
    i += 1


# for loop : iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
products = ["apple", "computer", "mobile", "laptop", "car"]
for item in products:
    print(item)


for char in "Python Programming Language":
    print(char)


# break, continue
for item in products:
    if item == "laptop": break
    if item == "apple" : continue
    print(item)


# range()
for i in range(4, 10):
    print(i)