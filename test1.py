import os

with open("test1.txt", 'r') as test:
    print(test.readline())
    print(type(test.readline()))
