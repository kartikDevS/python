def sum(n):
    if(n==0):
        return 0
    return n%10+sum(n//10)
        

n=int(input())


if(n<1000 and n>9999):
    print("Enter a four digit number")
else:
    a=sum(n)
    print(a)