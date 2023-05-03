import random
x=0
y=0
z=1
for i in range(1,10,1):
    lis=random.randint(1,50)
    print(lis)
    if lis > 10 and lis < 20:
        z += 1 
        y = y+lis
    elif lis > 30:
        x += 1
promedio= x/(z-1)
print ("El promedio es: ",y )
print ("Los nnumeros superiores a 30 son: ",x)
