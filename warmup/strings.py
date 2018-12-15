name = 'Brad'
age = 32

# Concatenate
print('Hello I am ' + name + ' and I am ' + str(age))


# Arguments by position
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in 3.6+)
print(f'My name is {name} and I am {age}')


# String Methods
s = 'Hello there world'

# Capitalize first letter
print(s.capitalize())

# Get length
len(s)

# Replace
s.replace('world', 'everyone')

# Count
s.count('h')

# Starts with
s.startswith('hello')

# Ends with
s.endswith('d')

# Is all alphanumeric
s.isalnum()

# Is all alphabetic
s.isalpha()

# Is all mumeric
s.isnumeric()
