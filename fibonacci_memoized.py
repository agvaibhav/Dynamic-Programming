def fib(n,lookup):
    if n==0 or n==1:
        lookup[n]=n

    if lookup[n] is None:
        lookup[n]=fib(n-1,lookup)+fib(n-2,lookup)

    return lookup[n]

def main(n):
   
    lookup=[None]*(n+1)

    print("fibonacci number is:",fib(n,lookup))

if __name__=="__main__":
    n=int(input("write the number you want to calculate fibonacci for:"))
    main(n)
          
