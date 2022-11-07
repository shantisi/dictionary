# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}

d = {}
a =int(input("Enter the size of main dictionary: "))
for i in range(a):
    key = input("enter the key name of main dictionary: ")
    size= int(input("Enter the size of nested dictionary: "))
    c={}
    for j in range (size):
        n = input("enter the name of key of child dictionary: ")
        value= input('Enter the value: ')
        c[n]=value
    d[key]=c
print(d)
    

num= [1, 2, 3, 4]
h={}
for i in  range (1,len(num)+1):
    h=({num[-i]:h})
print(h)

# o.p: {1: {2: {3: {4: {}}}}}

