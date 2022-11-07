# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary: {'S 001': ['Math', 'Science'], 'S 002': ['Math',
# 'English']}
# New dictionary: {'S001': ['Math', 'Science'], 'S002': ['Math',
# 'English']}


list ={'S 001': ['Math', 'Science'], 'S 002': ['Math',
'English']}
d={}
for i in list:
    sum=""
    for j in i:
        if j!=" ":
            sum=sum+j
    d.update({sum:list[i]})
print(d)

          


list=[1,2,1,2,1,3,2]
i=0
while i <len(list):
    j=0
    c=0
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
        else:
            pass
        j=j+1
    i=i+1
print(c)



list=[1,2,1,2,1,3,2]
i=0
a=[]
while i<len(list):
    if list [i] not in a:
        a.append (list[i])
    i=i+1
print(a)



x = int(input("enter"))
y = int(input("enter"))
z = int(input("enter"))
n = int(input("enter"))
b=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k==n:
                continue
            else:
                b.append([i,j,k])
print(b)


i = 1
while True:
    if i%3 == 0:
        break
    print(i)
 
    i+= 1