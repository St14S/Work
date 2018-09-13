# y = a*x**2+b*2 + c =0
print("Enter a")
a = int(input())
print("Enter b")
b = int(input())
print("Enter c")
c = int(input())
d = b**2 - 4*a*c
if d>0:
    print("d>0 ","x1 = ",(-b +d**0.5)/(2*a), "x2 = ",(-b -d**0.5)/(2*a))
elif d<0:
    print("d<0 ","No money")
if d==0:
    print("d=0 ","x1 = ",(-b)/(2*a))
