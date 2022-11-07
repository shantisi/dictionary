# Q10.Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are square of keys.

b={}
a=int(input("enter no"))
for i in range(a):
    n=int(input("enter no"))
    b.update({n:n*n})
print(b)