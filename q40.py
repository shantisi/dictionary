# Q40. Write a Python program to convert more than one list to nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
# {'S004': {'Saim Richards': 92}}]

d={}
a=int(input("enter the size of main dictionary"))
for i in range(a):
    key=input(' enter the key name')
    size=int(input ("enter the size of nested dict"))
    c={}
    for j in range (size):
        n=input("enter the name of key dict")
        value =input("enter the value")
        c[n]=value
    d[key]=c
print([d])
