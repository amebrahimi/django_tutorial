# Simple Dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Using a constructor
person = dict(first_name ='john', last_name='Doe', age=30)

# Access value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '444-444-4444'

# Get keys
print(person.keys())

# Get values
print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# Remove item
del(person['age'])
person2.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 40},
    {'name': 'Bob', 'age': 209}
]

print(people[1]['name'])

print(person)