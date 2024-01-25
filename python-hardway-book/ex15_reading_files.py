from sys import argv 

filename = argv[1]

with open(filename) as f:
    reader = f.read()
print(reader)
