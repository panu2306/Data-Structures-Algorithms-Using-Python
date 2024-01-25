from sys import argv 

print("We are going erase data of file and write new data to it")
print("To cancel hit ctrl+c")
print("To continue hit Enter")
input("?")

print("Opening a file")
f = open(argv[1], "w")
print("Erasing contents of file...")
f.truncate()

print("Let's write new text data to it")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

f.write(line1)
f.write("\n")
f.write(line2)
f.write("\n")
f.write(line3)
f.write("\n")

print("closing file...")
f.close()

