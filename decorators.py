#!/usr/bin/bash
# author = 'Kalyan Sankar'

#----- Custom Decorators -----

def generator_forloop(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        return [ i for i in result ]
    return wrapper

def generator_next(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        return [next(result) for _ in range(*args, **kwargs)]
    return wrapper
