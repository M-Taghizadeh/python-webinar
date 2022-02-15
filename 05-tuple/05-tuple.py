### [TUPLE]
# tuple is a collection which is define ordered(like list) and unchangeable. In Python tuples are written with round brackets.
my_tuple = ("banana", "apple", "orange", "cherry", "melon", "kiwi", "mango", "apple", "cherry")


# Access Item
print(my_tuple[1:3])


# Unchangeable
# my_tuple[1] = "computer" # Error


# Ordered
print(my_tuple)


# len
print(len(my_tuple))


# change tuple values :
year_tuple = ("2015", "2016", "2017", "2019")
year_list = list(year_tuple)
year_list[3] = "2018"
year_tuple = tuple(year_list)
print(year_tuple)


# join
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1 = t1 + t2
print(t1)


# multiply tuple
print(t1 * 3)


# unpack tuple
product_tuple = ("computer", "lenovo", "1000$", "2022")
(name, producer, price, year) = product_tuple
print(name, producer, price)


# loop
for item in product_tuple:
    print(item)


# methods
print(my_tuple.count("apple"))
print(my_tuple.index("apple"))