# why generator used? 
# 1) Generator use for iterate in iterable object(Lazy Iterator)
# 2) Increasing speed
# 3) Reduce memory usage
# 4) used in iterators(for while)

# yield
def show_product():
    yield 'laptop'
    yield 'computer'
    yield 'watch'
    yield 'pc'
    yield 'car'

print(show_product()) # <generator object>
for i in show_product():
    print(i)


# next()
products = show_product()
print(next(products))
print(next(products))


# for example

# Classical function
def get_even(n):
    num = 0
    evens = []
    while(num<n):
        if num % 2 == 0:
            evens.append(num)
        num = num + 1
    return evens

print(get_even(100))


# Generator : Lazy Iteration
def get_even_generator(n):
    num = 0
    while(num<n):
        if num % 2 == 0:
            yield num
        num = num + 1

even_numbers = get_even_generator(100)
print(next(even_numbers))
print(next(even_numbers))
print(next(even_numbers))
