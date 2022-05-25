x= int(input("Enter The Range for Fibunacci Numbers:"))
a=0
b=1

if x<=0:
     print("Please enter a valid Number")

elif x==1:
     print(a)

else:
     print(a)
     print(b)
     for i in range(2,x): #loop
        c=a+b
        a=b
        b=c
        print(c)