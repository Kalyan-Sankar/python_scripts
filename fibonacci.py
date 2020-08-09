#!/usr/bin/python python
#author='Kalyan Sankar'

from decorator import generator_result

#----- generate fibonacci series for a given 'n' number -----
@generator_result
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
