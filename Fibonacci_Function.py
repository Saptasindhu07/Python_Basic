import sys
def fibonaci(n):
    a=0
    b=1
    sys.stdout.write("0 1 1 ")
    for i in range(0,int(n)):
        copy=b
        b=a+b
        a=copy
        sys.stdout.write(str(a+b)+" ")
n=input("Enter number of terms: ")
print ("Required Fibonacci series: \n")
print(fibonaci(n))
        
        
        
        