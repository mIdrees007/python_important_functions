from functools import reduce


square = lambda a: a * a
print(square(5))


add= lambda a, b : a +b
print(add(4, 23))
def square(a):
    return a**2
print(square(4))


def is_even(n):
    return n % 2 == 0
# filter 
nums = [1, 32, 5, 6, 89, 9, 13, 15]

evens = list(filter(is_even,nums))
odd = list(filter(lambda n: n %2 != 0, nums))

#map 
def update(n):
    return n+2
doubles = list(map(update, odd))
tribles  = list(map(lambda n: n+3, evens))

square = list(map(lambda n : n**2, tribles))
def add_all(a, b):
    return a+b
sum = reduce(add_all, odd)

sub = reduce (lambda a, b : a -b, doubles)

print(evens)
print(tribles)
print(square)
print(odd)
print(sum)
print(doubles)
print(sub)