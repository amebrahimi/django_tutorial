
# Open a file
myFile = open('myfile.txt', 'w')


# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love python')
myFile.write(' and java script')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like Kotlin')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(10)
print(text)