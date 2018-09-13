x = int(input())
#print ("type x = ", type(x),"type y = ", type(y))
if x>0:
    print("x>0")
    if ((x>=-20)and(x<=-10)):
        print("(x>=-20)and(x<=-10)")
    elif ((x>=-10)and(x<=10)):
        print("(x>=-10)and(x<=10)")
    elif ((x>=10)and(x<=20)):
        print("(x>=10)and(x<=20)")
else:
     print("x<0")     

