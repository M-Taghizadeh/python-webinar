# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def say_hello(name, family):
    print(f"hello to {name} {family}")

say_hello("Mohammad", "Taghizadeh")
say_hello("Ali", "Mahmoodi")
say_hello("Ahmad", "Rezapour")


# Parameters or Arguments?
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# default Arguments
def show_user_info(name, last_name, age, email, country='iran'):
    print('name :', name)
    print('last name :', last_name)
    print('age :', age)
    print('email :', email)
    print('country :', country)

show_user_info('mohammad', 'taghizadeh', '22', 'taghizadeh@gmail.com')
show_user_info('mahsan', 'motahari', '21', 'mahsan@gmail.com', 'germany')


# *args : If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def show_product(*products):
    print(products[2:5])
show_product("laptop", "pc", "computer", "mobile", "iphone", "tablet")


# **kwargs
def show_user_info(**users):
    print(f"user's first name is {users['firstname']}")
    print(f"user's last name is {users['lastname']}")

show_user_info(firstname = "mahdi", lastname = "mahdavi")


# return value:
def get_avg(sum_numbers, sum_unit):
    avg = sum_numbers / sum_unit
    return avg

my_avg = get_avg(390, 20)
print("AVG :", my_avg)

 
#  Recursion ---> exp) Fibo Func : [0  1  1  2  3  5  8  13 …]
def fibo(number):
    if(number == 0 or number == 1):
        return number
    else:
        return fibo(number - 1) + fibo(number - 2)

number = int(input('Enter number :'))
for i in range(0, number):
    print(fibo(i))


# parameters : we can have any objects for parameters of functions : list tuple set dict , ...
def show_users(users_list):
    for user in users_list:
        print(user)

show_users(users_list= ["mohammad", "ahmad", "sara", "sina", "ali",])

