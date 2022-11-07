# Q23.Write a Python program to find the highest 3 values of corresponding keys in a
# # dictionary.
a={"a":100,"b":500,"c":300,"d":400,"e":300,"f":600,"g":700}
f=[]
w={}
d=[]
max1=0

max2=0
max3=0
for i in a:
    for j in a:
        if a[j]>max1:
            max1=a[j]
            n=j
        if a[j]>max2 and max1!=a[j]:
            max2=a[j]
            m=j
        if a[j]>max3 and max1!=a[j] and max2!=a[j]:
            max3=a[j]
            p=j
f.append(n)
f.append(m)
f.append(p)
d.append(max1)
d.append(max2)
d.append(max3)
for i in range (len(f)) :
    w.update({f[i]:d[i]})
print(w)