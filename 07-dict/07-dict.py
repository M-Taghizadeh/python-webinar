### [DICTIONARY]
# A dictionary is a collection which is ordered, changeable and indexed. (Key Value Data Structure...)
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# define
car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2022
}
print(car_dict)


# get value
print(car_dict.get("model"))
print(car_dict['brand'])


# keys()
car_dict_keys = car_dict.keys()
for item in car_dict.keys():
    print(item, car_dict[item])
car_dict["color"] = "white"
print(car_dict_keys)


# items() : key and values
for key, value in car_dict.items():
    print(key, value)


# len
print(len(car_dict))


# change value
car_dict['year'] = '2022'


# Power of Dict : Nested Dictionaries 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


# del remove copy ,....
