#!/usr/bin/python
# author = 'Kalyan Sankar'

from decorator import *

@output
def ReverseMat(mat, n):

    output=''

    for i in range(n):
        output+='\n'
        for j in range(n):
            x = str(mat[j][n-(i+1)])
            output+=x+" "

    return f'Reverse of a given matrix is: {output}'

mat=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
n=len(mat)

ReverseMat(mat,n)
