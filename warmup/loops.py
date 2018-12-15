people = ['john', 'Will', 'Janet', 'Karen']

# Simple for loop
for person in people:
    print('Current person: ', person)

# Break out
for person in people:
    print('Current person: ', person)
    if person == 'Janet':
        break

# Continue
for person in people:
    if person == 'Janet':
        continue
    print('Current person: ', person)

# Range
for i in range(len(people)):
    print('Current Person: ', people[i])

for i in range(0, 10):
    print('Number ', i)

count = 0
while count <= 10:
    print('Count: ', count)
    count += 1