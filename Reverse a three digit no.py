#reverse a three digit no
a=int(input('a=?'))
c=a%10
d=a//10
e=d%10
f=d//10
h=c*100+e*10+f
print("Reverse a three digit no:",h)
