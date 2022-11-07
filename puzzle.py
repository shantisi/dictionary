

door=int(input("enter no"))
close=0
open=0
while close<=open:
    for i in range(1,101):
        d=i*i
        if d<=door:
            open=open+1
        else:
            close=close+1    
print(close)

doors=int(input("enter no"))
z=1
close=0
open=0
while z<=doors:
    for i in range(1,101):
        d=z*z
        if d<=doors:
            open=open+1
        else:
            close=close+1
        z=z+1	
        print(open)

    d=[]
    i=1
    while i<=16:
        if i%3==0 and i%5==0:
            d.append("FizzBuzz")
        elif i%3==0:
            d.append("Fizz")
        elif i%5==0:
            d.append("Buzz")
        else:
            d.append(i)
        i=i+1
    print(d)




