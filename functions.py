# function is a block of code
def sayHello(name='johnny'):
    print(f'hello {name}')

# return values


def getSum(num1, num2):
    total = num1 + num2
    return total


sayHello('john doe')
print(getSum(1, 2))


# lambda function is a small anonymous function similar to an arrow function in JS
# getSum = lambda  num1, num2: num1 + num2
