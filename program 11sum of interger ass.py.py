# write program of finding sum of interger ,if two values are eaqual sum will be zero.
n1=int(input("enter a value of n1 :")) #enter a value 1
n2=int(input("enter a value of n2 :"))
n3=int(input("enter a value of n3 :"))

if(n1==n2):
    print("the sum will be zero")
elif(n2==n3):
    print("the sum will be zero")
elif(n3==n1):
    print("the sum will be zero")
else:
    print("sum of three integer: ",n1+n2+n3)
       