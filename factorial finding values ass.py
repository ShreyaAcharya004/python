#write a program python to get the factorial values.
n=int(input("enter a number:"))
fact=1
for i in range (1,n+1,1):
    fact= fact*i
print ("factorial of number:", fact)