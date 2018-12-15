# Create function
def sayHello(name='Sam'):
    """
    Prints hello and then name.
    """
    print('Hello ' + name)

# Return value


def getSum(num1, num2):
    total = num1 + num2
    return total


numSum = getSum(2, 3)

def addOneToNum(num):
    num += 1
    return num

num = 5
new_num = addOneToNum(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions.

getSum = lambda num1, num2 : num1 + num2
print(getSum(9,2))

addOneToNum = lambda num : num +1