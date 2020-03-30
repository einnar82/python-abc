# a dictionary is a collection which is unordered, changeable and indexed. No duplicate members
# just like JS Objects

person = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 30
}

print(person, type(person))
# get value

print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-55-55'
# get keys
print(person.keys())

# copy dictionary
person2 = person.copy()
person2['city'] = 'boston'

# remove item
del person['age']
person.pop('phone')

# length of dictionary
len(person)
# list of dictionary
people = [
    {
        'name': 'martha',
        'age': '30'
    },
    {
        'name': 'kevin',
        'age': '25'
    }
]
# destructuring in dictionaries
martha, kevin = people
print(kevin)
