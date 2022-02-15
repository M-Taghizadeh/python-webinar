# A set is a collection which is unordered, unchangeable, and unindexed.
# and do not allow duplicate values


my_set = {"title", "author", "date", "subject", "title", "title"}


# not allow duplicate values
print(my_set)


# unordered
# print(my_set[1]) # TypeError: 'set' object is not subscriptable


# Access items : for loop
for item in my_set:
    print(item)


# add item
my_set.add("content")


# Join Two Sets : update() or union()
# update --> Add multiple items to a set, using the update() method:
my_set.update(['1', '2', '3'])
my_set_new = my_set.union(['1', '2', '3'])
print(my_set)
print(my_set_new)


# len
print(len(my_set))


# remove
my_set.remove("content")
print(my_set)


# pop 
my_set.pop()
print(my_set)


# clear
my_set.clear()
print(my_set)


# del set
del my_set
print(my_set)


# set Methods
# add() : Adds an element to the set
# clear() :	Removes all the elements from the set
# copy() : Returns a copy of the set
# difference() : Returns a set containing the difference between two or more sets
# difference_update() : Removes the items in this set that are also included in another, specified set
# discard() : Remove the specified item
# intersection() : Returns a set, that is the intersection of two other sets
# intersection_update() : Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() : Returns whether two sets have a intersection or not
# issubset() : Returns whether another set contains this set or not
# issuperset() : Returns whether this set contains another set or not
# pop() : Removes an element from the set
# remove() : Removes the specified element
# symmetric_difference() : Returns a set with the symmetric differences of two sets
# symmetric_difference_update() : inserts the symmetric differences from this set and another
# union() : Return a set containing the union of sets
# update() : Update the set with the union of this set and others