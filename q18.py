# Write a Python program to sort a dictionary by key.

a={"a":100,"b":200,"c":300,"d":400,"e":500,"f":600,"g":700}
max=0
min=a["a"]
for i in a:
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]
print(max)
print(min)
