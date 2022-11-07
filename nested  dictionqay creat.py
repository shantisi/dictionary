a =int(input("Enter the size of main dictionary: "))
d={}
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
    