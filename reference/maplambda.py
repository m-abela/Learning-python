'''
lambda functions - single line function
mapping - applies function to each elemen in array
'''

#single argument
x = lambda a : a + 10
print(x(5))

#double argument
x = lambda a, b : a * b
print(x(5, 6))

##multiple arguments
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

##map example
def addition(n):
    return n + n

numbers = [1, 2, 3, 4]
result = map(addition, numbers)
print(list(result))

##map with lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

##2 numbers
numbers = [1, 2, 3, 4]
number2 = [2,3,4,5]
result = map(lambda x, y: x + y, numbers, number2)
print(list(result))
