# list is a collection of data, unordered or ordered
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pear']

print(numbers)
# print specific item in list
print(fruits[1])
# list length
print(len(fruits))
# add to list
fruits.append('mango')
# remove to list
fruits.remove('pear')
# insert to a specific position
fruits.insert(0, 'banana')
# remove with pop
fruits.pop(1)
print(fruits)
