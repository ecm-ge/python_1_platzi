#Modulos

import sys

print(sys.path)

import re

text = 'Mi numero es 3108840712'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,33,3,21]
counter = collections.Counter(numbers)
print(counter)