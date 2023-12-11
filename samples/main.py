import os
import sys
from validator import Validator
# The directory with XML files
XML_DIR = "."
file_name = sys.argv[1]

validator = Validator("./cap-library/schema/cap12.xsd")

#for file_name in os.listdir(XML_DIR):
print('{}: '.format(file_name), end='')

file_path = '{}/{}'.format(XML_DIR, file_name)

if validator.validate(file_path):
    print('Valid! :)')
else:
    print('Not valid! :(')

