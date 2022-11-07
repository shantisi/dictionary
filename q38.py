# Q38.. Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


list={'c1': 'Red', 'c2': 'Green', 'c3': None}
a={}
d= 'c3'
for key, value in list.items():
    if key is not d:
        a[key] = value
print(a)




d={"a":1,"b":2,"c":[{"A":11,"B":21}],"D":{"a":[1,2,9]}}
for i in d:
    if type (d[i])==dict:
        for j in d[i]:
            print(d[i][j][2])
for i in d:
    if type(d[i])==list:
        for j in range(len(d[i])):
            for k in d[i][j]:
                print(d[i][j][k])
 