# Core modules
import datetime
from datetime import date
import time
from time import time

# today = datetime.date.today()
today = date.today()

# timestamp = time.time()
timestamp = time()

print(timestamp)

# Pip module
import camelcase

camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))

# Custom modlues
import validator
from validator import validate_email

email = 'Khers'
if validate_email(email):
    print('Email is valid')
else:
    print('Not an email')

# pip install camelcase

# pip freeze - Shows all the modules installed