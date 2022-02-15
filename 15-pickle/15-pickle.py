import pickle


my_dict = {
    "name":"mohammad",
    "family":"taghizadeh",
    "age":"23"
}


# dump() : serializing objects
with open("data.dat", "wb") as f:
    pickle.dump(my_dict, f)

 
# load() : deserializing objects
with open("data.dat", "rb") as f:
    my_dict = pickle.load(f)
    print(my_dict, type(my_dict))