list_1=[] 
list_2=[]

x=(input("enter the values seperated by space for list 1:"))
list_1=x.split()

y=(input("enter the values seperated by space for list 2:"))
list_2=y.split()
print(list_1,list_2)


for  num in list_1:
    num=int(num)

    if num>=0:
        print(num,end=" ")
   
    


print("are the positive numbers in list 1 ")
     
for  num in list_2:
    num=int(num)

    if num>=0:
        print(num, end=" ")
        
print("are the positive numbers in list 2")
        
     

