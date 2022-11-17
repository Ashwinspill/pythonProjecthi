def fact(n):
    for i in range(1,n):
        if(n%i==0):
            print(i)
n=int(input("the number is : "))
fact(n)