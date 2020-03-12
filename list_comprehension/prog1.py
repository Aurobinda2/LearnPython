import functools

l1 = [1, 2, 3, 4, 5, 6]

list1 = [i for i in l1]

print list1

list2 = [i * i for i in l1]

print list2

list3 = [i for i in l1 if i % 2 == 0]

print list3

list4 = list(map(lambda x: x, "Aurobinda"))

print list4

list5 = list(filter(lambda x: x % 2 == 0, l1))

print list5

list6 = list(map(lambda x: x % 2 != 0, l1))

print list6

# factorial of a number
factorial = functools.reduce(lambda x, y: x * y, [i for i in range(1, 5)])

print factorial

# factorial number for a set of number

set_of_factorial_number = [functools.reduce(lambda x, y: x * y, [i for i in range(1, i + 1)]) for i in l1]

print set_of_factorial_number

# check prime number for a particular range
prime = filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, 5))
print prime

# ALL method

# all function return true if all value of a list is true or list is empty

print all([])

print all([True, True, True])

print all([False, False])

print all([True, False])


