# Q15.Write a Python program to remove a key from a dictionary.


a={1:"rani",2:"ram",3:"rina",4:"sonu",5:"golu"}
b={}
k=a[2]
for i in a:
  if k !=a[i]:
    b.update({i:a[i]})
print(b)