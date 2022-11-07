# Q8.
# Write a Python program to check whether a given key already exists in a dictionary.

a=(input("enter key"))
d = {'a': 100, 'b': 200, 'c':300}
if a in d:
    print("yes")
else:
    print("no")