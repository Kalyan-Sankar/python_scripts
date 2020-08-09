#!/usr/bin/env python
# author='Kalyan Sankar'

#-----decorator(@generator_result) to use for generators-----

def generator_result(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        return [ i for i in result ]
    return wrapper
