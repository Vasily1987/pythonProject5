#МОДУЛЬ 1

def long_separator(count):
    return '*' * count
print(long_separator(5))

def simple_separator():
    return long_separator(5)
print(simple_separator())


def separator(simbol, count):
    return simbol*count
print(separator('-',10))


def hello_world():
    print(separator('*',10))
    print()
    print('Hello World!')
    print()
    print(separator('#',10))

hello_world()



def hello_who(who='World'):
    print(separator('*', 10))
    print()
    print(f'Hello {who}!')
    print()
    print(separator('#', 10))
hello_who('Max')
hello_who()


def pow_many(power, *args):
    return sum(args)**power
print(pow_many(2,1,1))
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    for h,k in kwargs.items():
        print(f' {h}, -->, {k}')

print_key_val(name='Max', age=21)

print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    result = []
    for i in iterable:
        if function(i):
            result.append(i)
    return result

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True

