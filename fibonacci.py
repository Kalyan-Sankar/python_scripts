#!/usr/bin/python python
# author='Kalyan Sankar'

from decorator import *

#----- generate fibonacci series for a given 'n' number using generator -----
@generator_next        # use any one decorator
@generator_forloop     # use any one decorator
def Fib(n):
    count=0
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
        if (count==n):
            break
        count+=1

n=9
print (f'Fibonacci series for a given number {n} are {Fib(9)}')

#----- generate fibonacci series for a given 'n' number using normal function -----
def Fib(n):

    if n < 0:
        print ("Input Integer should greater than 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        result=Fib(n-1)+Fib(n-2)
        return result

n=9
print (f'Fibonacci series for a given number {n} is {Fib(9)}')

# ----- another example -----
FibArr=[0,1]
def Fib(n):

    if n < 0:
        print ("Input Integer should greater than 0")
    elif n <= len(FibArr):
        return FibArr[n-1]
    else:
        result=Fib(n-1)+Fib(n-2)
        FibArr.append(result)
        return result
n=9
print (f'Fibonacci series for a given number {n} is {Fib(9)}, series {FibArr}')
