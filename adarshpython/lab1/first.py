# To find the factorial
nums=int(input("enter a number:"))
fact=1
if num<0:
    print("factorial is not defined for negative numbers")
elif num==0 or num==1:
    print("Factorial of", num ,"is 1")
else: 
    for i in range(1,n+1):
        fact*=i
    print("Factorial of ",num," is ",fact)   
# to check for prime 
n=int(input("enter a number:"))
if n<=1:
    print("not prime")
else:
    is_prime=True
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            is_prime=False 
            break
    if is_prime:
        print(n," is a prime number")
    else:
        print(n," is not a prime number")    
                
