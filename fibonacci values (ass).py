#write program python to get fibonacci series.
n=int(input("enter a number:")) 

# enter first two terms
n1,n2=0,1
count=0

print ("fibonacci sequenece:")
for i in range (1,n+1,1):
    print (n1)
    fib=n1+n2
    
    
    n1= n2
    n2=fib
    