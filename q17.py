# Write a Python program to sort a dictionary by key.

a={17:2,12:3,23:4,4:5,5:6}
b=sorted(a.keys())
c={}
for i in b:
    for j in a:
        if i==j:
            c.update({j:a[j]})
print(c)



