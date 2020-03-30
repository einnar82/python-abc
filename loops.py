people = ['john', 'paul', 'sarah', 'susan']

for person in people:
    print(f'Current person: {person}')

# break the loop
for person in people:
    if person == 'sarah':
        break
    print(f'Current person: {person}')

# continue the loop
for person in people:
    if person == 'sarah':
        continue
    print(f'Current person: {person}')

# range
for i in range(len(people)):
    print(people[i])

# while loop
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
