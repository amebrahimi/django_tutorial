x = 10
y = 10

# Simple if
if x == y:
    print(f'{x} is equal to {y}')


# If/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is less than 2 and greater than 10')

# and
if x > 2 and x <= 10:
    print(f'{x} is less than 2 and greater than 10')

# or
if x > 2 or x <= 10:
    print(f'{x} is less than 2 and greater than 10')

# not
if not(x == y):
    print(f'{x} is not equal to {y}')


numbers = [1,2,3,4,5,10]

# in
if x in numbers:
    print(x in numbers)

# not in
if x not in numbers:
    print(x in numbers)

# is
if x is y:
    print(x is y)

# is not 
if x is not y:
    print(x is not y)