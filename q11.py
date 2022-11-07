# Q11.Write a Python script to merge two Python dictionarie.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
for i in d2:
    d1.update(d2)
print(d1)
