import numpy as np

a = np.array([1, 2])
b = np.ones(2, dtype=int)
"""  
[ 1  2 ]   
+             -            *         / 
[ 1  1 ]
=
[ 2  3 ]       [ 0 1 ]    [ 1 2 ]  [ 1 2]
"""
print( a + b)
print( a - b)
print( a * b)
print( a / b)


