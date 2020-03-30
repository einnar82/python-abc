x = 1
y = 2
name = 'john'
age = 10

if x > y:
    print(f'x is greater than y')

# if else
# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# else if
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{y} is greater than {x}')

# Logical operators (and, or)

if name == 'john' and age == 10:
    print(True)

if name == 'john' or age == 10:
    print(True)

if not(x == y):
    print(True)


fruits = ['apple', 'mango', 'pear']

if 'apple' in fruits:
    print('Apple is in the fruits.')
