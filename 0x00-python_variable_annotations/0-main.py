#!/usr/bin/python3
"""
This is the execution file for the 0-add task
"""
add = __import__("0-add").add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
# Expected output:
# {'a': float, 'b': float, 'return': float}
