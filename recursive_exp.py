# we have to write a recursive function for calculating the exponent of a number n raise to the power m

n=int(input())
m=int(input())
def exp(n,m):  
    if(m==0):
        return 1
    return n*exp(n,m-1)
if(n<=0):
    print("Please enter a postive integer")
else:
    a=exp(n,m)
    print(a)



