# Q13.Write a Python program to sum all the items in a dictionary.

a={1:2,3:4,5:6,7:8,9:10,10:11}
sum=0
b={}
for i in a:
    sum=sum+a[i]
print(sum)